from django.views.generic import ListView, DetailView
from .models import Book, Author
from django.db.models import Q, F
# Create your views here.


class HomeView(ListView):
    model = Book
    template_name = 'book/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_book"] = Book.objects.all().order_by("-data_of_production")
        context["popular_book"] = Book.objects.all().order_by("-views_count")
        return context


class BookList(ListView):
    model = Book
    paginate_by = 5


class BookDetail(DetailView):
    model = Book

    def get_object(self, queryset=None):
        book_object = super().get_object()
        book_object.view_count = F('view_count') + 1
        book_object.save()

        return book_object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['book_series'] = Book.objects.filter(Q(series=self.get_object().series)).filter(~Q(series=""))

        if Book.objects.filter(Q(series=self.get_object().series)).filter(~Q(series="")):
            context['book_category'] = Book.objects.filter(Q(category=self.get_object().category)).exclude(
                Q(series=self.get_object().series))
        else:
            context['book_category'] = Book.objects.filter(Q(category=self.get_object().category))

        return context


class BookCategory(ListView):
    model = Book
    paginate_by = 5

    def get_queryset(self):
        self.category = self.kwargs['category']
        return Book.objects.filter(category=self.category)


class BookSearch(ListView):
    model = Book
    paginate_by = 5
    template_name = 'book/search.html'

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


class AuthorDetail(DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_books'] = Book.objects.filter(author=self.get_object())
        return context
