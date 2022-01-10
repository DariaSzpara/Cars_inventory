from django.db import models

from book.models import Book
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book', null=True)
    publication_date = models.DateField()
    number_ISBN = 
    number_page =
    link_to_the_cover = 
    publication_language = models.CharField(max_length=100)

    
    