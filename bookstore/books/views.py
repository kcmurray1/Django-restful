from rest_framework import generics
from books.models import Book
from books.serializers import BookSerializer

"""
Create: POST /books
List: GET /books
"""
# collection view
# supports POST and GET requests "Create/View"
class BookCollection(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

"""
READ: GET /books/:id RETRIEVE
Update: PUT /books/:id UPDATE
Delete: DELETE /books/:id DESTROY
"""
# record view
class BookRecord(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer