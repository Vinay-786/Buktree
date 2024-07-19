from django import forms
from .models import Book, Chapter


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'published_date']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['author'].widget.attrs.update({'class': 'form-control'})
        self.fields['published_date'].widget.attrs.update(
            {'class': 'form-control'})


class ChapterForm(forms.ModelForm):
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
        super(ChapterForm, self).__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.all().order_by('title')

    def clean_order(self):
        order = self.cleaned_data.get('order')
        if order <= 0:
            raise forms.ValidationError("Order must be a positive integer.")
        return order
