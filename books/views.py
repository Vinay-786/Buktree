from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, ChapterForm, ResetForm
from django.contrib.auth.decorators import login_required
from .models import Book, Chapter


def home(request):
    books = Book.objects.all()[0:4]
    return render(request, "books/home.html", {"books": books})


def addchapter(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a view showing the list of books
            return redirect("home")
    else:
        form = BookForm()
    return render(request, "books/newadd.html", {"form": form})


def book_detail(request, book_id, chapter_id=None):
    book = Book.objects.get(pk=book_id)
    chapters = book.chapters.all()

    chapter_content = None
    if chapter_id:
        chapter = get_object_or_404(Chapter, pk=chapter_id, book=book)
        chapter_content = chapter.content

    context = {
        "book": book,
        "chapters": chapters,
        "chapter_content": chapter_content,
        "selected_chapter_id": chapter_id
    }
    return render(request, "book_details.html", context)


def explore(request):
    books = Book.objects.all()
    return render(request, "explore.html", {"books": books})


@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()
            # Redirect to a view showing the list of books
            return redirect("home")
    else:
        form = BookForm()
    return render(request, "add_book_v2.html", {"form": form})


@login_required
def add_chapter(request):
    if request.method == "POST":
        form = ChapterForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ChapterForm(user=request.user)
    return render(request, "add_chapter_v2.html", {"form": form})


def tandc(request):
    return render(request, "termsandcondition.html")


def bookload(request):
    return render(request, "bookload.html")


def resetpass(request):
    form = ResetForm()
    return render(request, "registration/password_reset_form.html",
                  {"form": form})


def profile(request):
    user = request.user
    books = user.books.all()
    return render(request, "profile.html", {"books": books})
