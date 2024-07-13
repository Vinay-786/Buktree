from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("explore", views.explore, name="explore"),
    path("addbook", views.addbook, name="addbook"),
]
