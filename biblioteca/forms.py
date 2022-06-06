from dataclasses import fields
from django import forms 
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['name', 'category', 'book_cover', 'author', 'publication_date', 'pages']