from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, ChapterForm, FeedbackForm
from django.contrib.auth.decorators import login_required
from .models import Book, Chapter
from django.contrib.auth import get_user_model

User = get_user_model()


def home(request):
    books = Book.objects.filter(verified=True).order_by(
        "published_date").reverse()[0:8]
    return render(request, "books/home.html", {"books": books})


def book_detail(request, book_id, chapter_id=None):
    book = get_object_or_404(Book, pk=book_id)
    chapters = book.chapters.all().order_by('order')
    chapter_content = None
    prev_chapter = None
    next_chapter = None

    if chapter_id:
        current_chapter = get_object_or_404(Chapter, pk=chapter_id, book=book)
        chapter_content = current_chapter.content
        prev_chapter = chapters.filter(order__lt=current_chapter.order).last()
        next_chapter = chapters.filter(order__gt=current_chapter.order).first()
    else:
        current_chapter = chapters.first()
        if current_chapter:
            chapter_content = current_chapter.content
            next_chapter = chapters.exclude(pk=current_chapter.pk).first()

    context = {
        "book": book,
        "chapters": chapters,
        "chapter_content": chapter_content,
        "selected_chapter_id": chapter_id if chapter_id else (current_chapter.id if current_chapter else None),
        "prev_chapter": prev_chapter,
        "next_chapter": next_chapter,
    }
    return render(request, "book_details.html", context)


def explore(request):
    bookquery = request.GET.get("q",)
    if bookquery:
        try:
            books = Book.objects.filter(
                title__icontains=bookquery, verified=True)
            users = User.objects.filter(username__icontains=bookquery)
            if users.exists():
                books = Book.objects.filter(author__in=users, verified=True)
        except User.DoesNotExist or Book.DoesNotExist:
            books = Book.objects.none()
    else:
        books = Book.objects.filter(verified=True)

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


def profile(request):
    user = request.user
    books = user.books.all()
    return render(request, "profile.html", {"books": books})


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = FeedbackForm()
    return render(request, "contactus.html", {"form": form})
