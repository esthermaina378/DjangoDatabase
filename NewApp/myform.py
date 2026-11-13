from django import forms

from NewApp.models import Book

# django forms
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'isbn', 'cost', 'category', 'year', 'published', 'cover')
