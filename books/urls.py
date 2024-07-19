from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("chapter", views.addchapter, name="chapter"),
    path("explore", views.explore, name="explore"),
    path("addbook", views.add_book, name="addbook"),
    path("addchapter", views.add_chapter, name="addchapter"),
]
