from django.urls import path

from .views import BookList, BookDetail, BookCategory, BookSearch, AuthorList, AuthorDetail

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('category/<str:category>', BookCategory.as_view(), name='book_category'),
    path('search/', BookSearch.as_view(), name='book_search'),
    path('<slug:slug>', BookDetail.as_view(), name='book_detail'),
    path('author/', AuthorList.as_view(), name='author_list'),
    path('author/<slug:slug>', AuthorDetail.as_view(), name='author_detail'),


]


