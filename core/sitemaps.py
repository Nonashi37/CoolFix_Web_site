from django.contrib.sitemaps import Sitemap
from django.urls import reverse
# Импортируем твой словарь данных, чтобы вытащить ключи-слаги
from .views import SERVICES_DATA 

class CoolFixSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"

    def items(self):
        # Собираем список кортежей: (имя_роута, слаг или None, приоритет, язык)
        urls = [
            ("home", None, 1.0, "ru"),       # Главная на русском
            ("home_ky", None, 0.9, "ky"),    # Главная на кыргызском
        ]
        
        # Динамически добавляем наши 4 новые страницы услуг для обоих языков
        for slug in SERVICES_DATA.keys():
            urls.append(("service_detail", slug, 0.8, "ru"))
            urls.append(("service_detail_ky", slug, 0.8, "ky"))
            
        return urls

    def priority(self, item):
        return item[2] # Возвращает приоритет (1.0, 0.9 или 0.8)

    def location(self, item):
        route_name, slug, _, _ = item
        if slug:
            # Если есть слаг, передаем его в reverse (например, /services/refrigerators-freezers/)
            return reverse(route_name, args=[slug])
        # Если слага нет, просто возвращаем путь к главной (например, / или /ky/)
        return reverse(route_name)