from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
from django.db.models import Q
# Create your views here.

class BookList(ListView):
    model = Book
    paginate_by = 5

class BookDetail(DetailView):
    model = Book
    # def get_object(self, queryset=None):
    #     object = super(BookDetail, self).get_object()
    #     object.views_count += 1
    #     object.save()
    #     return object


    def get_context_data(self, **kwargs):
        context = super(BookDetail, self).get_context_data(**kwargs)
        context['book_series'] = Book.objects.filter(series=self.get_object().series)
        context['book_category'] = Book.objects.filter(category=self.get_object().category).filter(~Q(series=self.get_object().series))
        return context


class BookCategory(ListView):
    model = Book

    def get_object(self, queryset=None):
        pass

    def get_context_data(self, **kwargs):
        context = super(BookDetail, self).get_context_data(**kwargs)
        context['book_category'] = Book.objects.filter(category=self.get_object().category)
        return context