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
    path("sendmail", views.ResetPass, name="sendmail"),
    path("bookdetail/<int:book_id>", views.book_detail, name="bookdetail"),
    path("resetpass", views.resetpass, name="resetmail")
]
