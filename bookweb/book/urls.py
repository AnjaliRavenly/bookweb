from django.urls import include, path

from .views import BookList, BookDetail, BookCategory, BookSearch, AuthorList, AuthorDetail

author_patterns = [
    path('', AuthorList.as_view(), name='author_list'),
    path('<slug:slug>/', AuthorDetail.as_view(), name='author_detail'),
]

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('category/<str:category>', BookCategory.as_view(), name='book_category'),
    path('search/', BookSearch.as_view(), name='book_search'),
    path('<slug:slug>', BookDetail.as_view(), name='book_detail'),

    path('author/', include(author_patterns)),


]


