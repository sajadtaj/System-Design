from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from books.models import Book
from .serializers import BookSerializer
# Create your views here.


class BookApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer