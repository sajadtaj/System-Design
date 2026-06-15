from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"