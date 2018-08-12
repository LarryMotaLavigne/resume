from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class MainView(TemplateView):
    template_name = "main.html"


class ExperiencesView(TemplateView):
    template_name = "experiences.html"


class InfoView(TemplateView):
    template_name = "info.html"


class PassionsView(TemplateView):
    template_name = "passions.html"


class PresentationView(TemplateView):
    template_name = 'presentations/example.html'


index = IndexView.as_view()
main = MainView.as_view()
experiences = ExperiencesView.as_view()
info = InfoView.as_view()
passions = PassionsView.as_view()
presentations = PresentationView.as_view()


# =========================================================================
# Error Pages
# =========================================================================

def handler404(request, exception, template_name='error_pages/404.html'):
    return render(request, template_name, status=404)


def handler500(request, exception, template_name='error_pages/500.html'):
    return render(request, template_name, status=404)
