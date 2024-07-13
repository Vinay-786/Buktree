from django.shortcuts import render


def home(request):
    return render(request, "books/home.html")


def contact(request):
    return render(request, "contact.html")


def explore(request):
    return render(request, "explore.html")


def addbook(request):
    return render(request, "addbook.html")


def passReset(request):
    pass
