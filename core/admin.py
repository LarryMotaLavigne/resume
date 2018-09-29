from django.contrib import admin
from django.contrib.sites.models import Site

from core.models import Contact

admin.site.unregister(Site)


@admin.register(Site)
class Sites(admin.ModelAdmin):
    list_display = ["id", "domain", "name"]


admin.site.site_header = "resume Administration"
admin.site.site_title = "resume Administration"


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "headline", "count", "last_connection"]
