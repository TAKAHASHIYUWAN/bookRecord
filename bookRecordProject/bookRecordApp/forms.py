from django import forms
from .models import Book

class BookImageForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('image',)