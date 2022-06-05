from django.db import models

# Create your models here.
class Livro(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    book_cover = models.ImageField(upload_to='images')
    author = models.CharField(max_length=255)
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    # pages = models.DecimalField(max_digits=None, decimal_places=0)
    pages = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)