from rest_framework import generics
from books.models import Book, Comment
from books.serializers import BookSerializer, CommentSerializer, RatingSerializer


class RatingCollection(generics.CreateAPIView):
    serializer_class = RatingSerializer


"""
Create: POST /books
List: GET /books
"""
# collection view
# supports POST and GET requests "Create/View"
class BookCollection(generics.ListCreateAPIView):
    # queryset is the set of rows in a table that we can reach
    # in this case Book.objects.all() lets us access any row
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


class CommentCollection(generics.CreateAPIView):
    # queryset = Book.objects.all()
    serializer_class = CommentSerializer


# Read comment GET /comments/:id
class CommentRecord(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = BookSerializer