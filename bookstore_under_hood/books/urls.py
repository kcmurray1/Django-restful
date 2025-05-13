from django.urls import path
from books.views import book_collection

urlpatterns = [
    path('books', book_collection)
 ]