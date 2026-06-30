# core/sitemaps.py — create this file

from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class CoolFixSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"

    def items(self):
        return [
            ("home",    1.0),   # Russian home — highest priority
            ("home_ky", 0.9),   # Kyrgyz home
        ]

    def priority(self, item):
        return item[1]

    def location(self, item):
        return reverse(item[0])