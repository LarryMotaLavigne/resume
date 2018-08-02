import logging

from django.db.models import F
from django.shortcuts import redirect
from linkedin import linkedin

from CV.settings import LINKEDIN_APPLICATION_KEY, LINKEDIN_APPLICATION_SECRET, LINKEDIN_APPLICATION_RETURN_CALLBACK, \
    URL_WITH_LINKEDIN_AUTH, URL_WITHOUT_LINKEDIN_AUTH
from core.models import Contact

logger = logging.getLogger("middleware")


class LinkedinMiddleware(object):

    def __init__(self, get_response):
        """
        Init the middleware with the response and the linkedin authentication object
        :param get_response: the middleware response
        """
        self.get_response = get_response
        self.authentication = linkedin.LinkedInAuthentication(LINKEDIN_APPLICATION_KEY,
                                                              LINKEDIN_APPLICATION_SECRET,
                                                              LINKEDIN_APPLICATION_RETURN_CALLBACK,
                                                              ['r_basicprofile'])

    def __call__(self, request):
        """
        Process the middleware request
        :param request: the request
        :return: if the page is not index, we force a linkedin authentication, else we return the response if the url is None
        """
        response = self.get_response(request)
        if request.resolver_match is not None:
            name = request.resolver_match.url_name
            logger.debug("----- ENDPOINT : " + str(name))
            if name in URL_WITH_LINKEDIN_AUTH and name not in URL_WITHOUT_LINKEDIN_AUTH:
                return self.process_linkedin_authentication(request)
        return response

    def process_linkedin_authentication(self, request):
        """
        Process a LinkedIn Authentication
        :param request: the request
        :return: if we have the authorization_code, we process the response.
        If we don't have this code, we have to parse the URL to retrieve the authorization code
        """
        logger.debug("AUTH CODE :" + str(self.authentication.authorization_code))
        # Exemple from the request : 'http://localhost:5000/?code=AQQFXVgx-5EHkyxBNMdQOyAIowfYy-uPr4AcdyKmf0FiGr7Co3BP1IgqjgyqqdyLHr8Ckpawpce_1ZeNDd7n54CFnmwbufQI1OTe9MyWO1Q8SK2njxPJzfPo8qr0hjepEZ22oR0khhkjIffzBLdHBu7fZfyGFQ&state=a3b257ba95561f6a1809fd8337b220c8#!'
        if self.authentication.authorization_code is None:
            url_datas = request.build_absolute_uri().split('?code=', 1)
            if len(url_datas) != 2:
                logger.debug("Not authentified yet, redirect to the authorization URL : " + str(
                    self.authentication.authorization_url))
                return redirect(self.authentication.authorization_url)
            else:
                auth_code = url_datas[1].split('&state=')[0]
                self.authentication.authorization_code = auth_code
                result = self.authentication.get_access_token()
                logger.debug("We have the TOKEN : " + str(result.access_token))
                application = linkedin.LinkedInApplication(token=result.access_token)
                self.get_resume_info(request, application)
                return redirect(request.resolver_match.url_name)  # To change to access other pages
        return self.get_response(request)

    @staticmethod
    def get_resume_info(request, application):
        """
        Get full information from a resume and add theses information to the session cache
        :param request: the request
        :param application: the application filled with access token
        """
        data = application.get_profile()
        logger.debug("Resume Data : " + str(data))
        request.session['firstName'] = data.get('firstName')
        request.session['lastName'] = data.get('lastName')
        request.session['headline'] = data.get('headline')
        contact, created = Contact.objects.get_or_create(first_name=data.get('firstName'), last_name=data.get('lastName'), headline=data.get('headline'))
        if not created:
            logger.debug("Not created :" + str(contact.count))
            contact.count = contact.count + 1
            logger.debug("New count :" + str(contact.count))
            contact.save()
