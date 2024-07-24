from django.shortcuts import render, redirect
from .forms import BookForm, ChapterForm


def home(request):
    return render(request, "books/home.html")


def addchapter(request):
    return render(request, "books/newadd.html")


def explore(request):
    return render(request, "explore.html")


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a view showing the list of books
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


def add_chapter(request):
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ChapterForm()
    return render(request, 'add_chapter.html', {'form': form})


def passReset(request):
    pass
