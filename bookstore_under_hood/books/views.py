from django.shortcuts import render
from books.models import Book
from books.serializers import BookSerializer, CommentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

class JSONResponse(HttpResponse):
    def __init__(self, content, **headers):
        


@csrf_exempt
def book_collection(request):
    if request.method == "GET":
        books = Book.objects.all()
        book_serializer = BookSerializer(books, many=True)
        body = JSONRenderer().render(book_serializer.data)

        headers = {}

        headers['content_type'] = 'application/json'

        return HttpResponse(body, **headers)
    elif request.method == "POST":
        book_data = JSONParser().parse(request)
        book_sr = BookSerializer(data=book_data)

        if book_sr.is_valid():
            book_sr.save()
            body = JSONRenderer().render(book_sr.data)

            headers = {}

            headers['content_type'] = 'application/json'
            headers['status'] = status.HTTP_201_CREATED

            return HttpResponse(body, **headers)
        else:
            body = JSONRenderer.render(book_serializer.errors)
            
            headers['content_type'] = 'application/json'
            headers['status'] = status.HTTP_400_BAD_REQUEST

            return HttpResponse(body, **headers)
    else:
        headers['content_type'] = 'application/json'
        headers['status'] = status.HTTP_400_BAD_REQUEST

        return HttpResponse(body, **headers)



# Create Comment: POST /comments
class CommentCollection(generics.)