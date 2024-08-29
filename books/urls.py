from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path("chapter", views.addchapter, name="chapter"),

    path("explore", views.explore, name="explore"),

    path("addbook", views.add_book, name="addbook"),

    path("addchapter", views.add_chapter, name="addchapter"),

    path("tandc", views.tandc, name="termsandcondition"),

    path("bookload", views.bookload, name="bookload"),

    path("bookdetail/<int:book_id>", views.book_detail, name="bookdetail"),

    path("bookdetail/<int:book_id>/<int:chapter_id>",
         views.book_detail, name="bookdetail"),

    path("profile", views.profile, name="profile")
]
