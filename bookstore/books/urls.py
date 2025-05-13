# application specific for REST-API related URL
from django.urls import path
from books.views import BookCollection, BookRecord, CommentCollection, CommentRecord, RatingCollection

urlpatterns = [
    # route, view to forward to BookCollections
    path('books', BookCollection.as_view()),
    path('books/<int:pk>', BookRecord.as_view()),
    path('comments', CommentCollection.as_view()),
    path('comments/<int:pk>', CommentRecord.as_view(), name="comment-record"),
    path('ratings', RatingCollection.as_view())
]