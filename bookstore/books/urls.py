# application specific for REST-API related URL
from django.urls import path
from books.views import BookCollection, BookRecord

urlpatterns = [
    # route, view to forward to BookCollections
    path('books', BookCollection.as_view()),
    path('books/<int:pk>', BookRecord.as_view())
]