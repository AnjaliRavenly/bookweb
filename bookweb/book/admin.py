from django.contrib import admin

# Register your models here.
from .models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'series')
    ordering = ('author',)
    search_fields = ('title', 'author')


# admin.site.register(Book)
admin.site.register(Author)


