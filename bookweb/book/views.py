from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
# Create your views here.

class BookList(ListView):
    model = Book


class BookDetail(DetailView):
    model = Book