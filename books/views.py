from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, ChapterForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Book


def home(request):
    books = Book.objects.all()[0:4]
    return render(request, "books/home.html", {"books": books})


def addchapter(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a view showing the list of books
            return redirect('home')
    else:
        form = BookForm()
    return render(request, "books/newadd.html", {'form': form})


def book_detail(request, book_id):
    _ = Book.objects.get(id=book_id)
    pass


def explore(request):
    books = Book.objects.all()
    return render(request, "explore.html", {"books": books})


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a view showing the list of books
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


@login_required
def add_chapter(request):
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ChapterForm()
    return render(request, 'add_chapter.html', {'form': form})


def tandc(request):
    return render(request, "termsandcondition.html")


def ResetPass(request):
    subject = "Test mail"
    message = "from vinay"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [""]
    send_mail(subject, message, email_from, recipient_list)
    return redirect("home")


def bookload(request):
    return render(request, "bookload.html")
