from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("ky/", views.home_ky, name="home_ky"),

    # Same view, different `lang` injected via the third path() argument —
    # no duplicated view logic, no if/else language branching at runtime.
    path("services/<slug:service_slug>/", views.service_detail_page,
         {"lang": "ru"}, name="service_detail"),
    path("ky/services/<slug:service_slug>/", views.service_detail_page,
         {"lang": "ky"}, name="service_detail_ky"),

    path("lang/<str:lang>/", views.set_language, name="set_language"),
]