from rest_framework import serializers
from books.models import Book


# All fields in Book model should be serialized into a dictionary
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'