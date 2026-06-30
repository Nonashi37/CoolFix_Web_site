from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from core.sitemaps import CoolFixSitemap

sitemaps = {
    "static": CoolFixSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),

    path("", include("core.urls")),
]
