from django.urls import path

from .views import BookList, BookDetail, BookCategory, BookSearch

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('category/<str:category>', BookCategory.as_view(), name='book_category'),
    path('search/', BookSearch.as_view(), name='book_search'),
    path('<slug:slug>', BookDetail.as_view(), name='book_detail'),
]


