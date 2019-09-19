from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Author
from django.db.models import Q
# Create your views here.

class HomeView(ListView):
    model = Book
    template_name = 'book/home.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["new_book"] = Book.objects.all().order_by("-data_of_production")
        context["popular_book"] = Book.objects.all().order_by("-views_count")
        return context


class BookList(ListView):
    model = Book
    paginate_by = 5


class BookDetail(DetailView):
    model = Book
    def get_object(self, queryset=None):
        object = super(BookDetail, self).get_object()
        object.views_count += 1
        object.save()
        return object


    def get_context_data(self, **kwargs):
        context = super(BookDetail, self).get_context_data(**kwargs)
        context['book_series'] = Book.objects.filter(series=self.get_object().series)
        context['book_category'] = Book.objects.filter(category=self.get_object().category).filter(~Q(series=self.get_object().series))
        print(context['book_series'])
        return context


class BookCategory(ListView):
    model = Book
    paginate_by = 5


    def get_queryset(self):
        self.category = self.kwargs['category']
        return Book.objects.filter(category=self.category)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookCategory, self).get_context_data(**kwargs)
        context["book_category"] = self.category
        return context


class BookSearch(ListView):
    model = Book
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(Q(title__icontains=query) | (Q(author__author__icontains=query)))
        else:
            object_list = self.model.objects.none()
        return object_list


class AuthorList(ListView):
    model = Author
    paginate_by = 5
    template_name = 'book/author_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AuthorList, self).get_context_data(**kwargs)
        # context["author_list"] = Author.objects.all().order_by("author")
        return context


class AuthorDetail(DetailView):
    model = Author
    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        context['author_books'] = Book.objects.filter(author=self.get_object())
        print("książki autora", context['author_books'])
        return context