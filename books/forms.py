from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Chapter


class BookForm(forms.ModelForm, LoginRequiredMixin):
    class Meta:
        model = Book
        fields = ['title', 'description',
                  'published_date', "book_cover"]
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['book_cover'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['published_date'].widget.attrs.update(
            {'class': 'form-control'})


class ChapterForm(forms.ModelForm, LoginRequiredMixin):
    class Meta:
        model = Chapter
        fields = ['name', 'book', 'content', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'book': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ChapterForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['book'].queryset = user.books.all().order_by('title')

    def clean_order(self):
        order = self.cleaned_data.get('order')
        if order <= 0:
            raise forms.ValidationError("Order must be a positive integer.")
        return order
