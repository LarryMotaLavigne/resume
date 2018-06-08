from django.contrib import admin

# Register your models here.
from django.contrib.sites.models import Site

admin.site.unregister(Site)


@admin.register(Site)
class Sites(admin.ModelAdmin):
    list_display = ["id", "domain", "name"]


admin.site.site_header = "CV Administration"
admin.site.site_title = "CV Administration"
