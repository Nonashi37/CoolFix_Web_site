from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("lang/<str:lang>/", views.set_language, name="set_language"),  # ← new
]