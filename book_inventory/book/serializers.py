from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = (
            'title',
            'author',
            'publication_date',
            'number_ISBN'
            'number_pages'
            'link_to_the_cover'
            'publication_languange'
        )