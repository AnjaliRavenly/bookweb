from django.db import models
from django.utils.text import slugify
import json

# Create your models here.

class Author(models.Model):
    author = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100)
    image = models.ImageField(upload_to='authors')
    description = models.TextField(max_length=1000)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.author)
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.author


CATEGORY_BOOKS = {
    ("fantasy", "FANTASY"),
    ("sci_fi", "SCI_FI"),
    ("horror", "HORROR"),
    ("biographies", "BIOGRAPHIES"),
    ("romance", "ROMANCE"),
    ("thrillers", "THRILLER"),
}

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books')
    data_of_production = models.DateField()
    category = models.CharField(choices=CATEGORY_BOOKS, max_length=15)
    description = models.TextField(max_length=1000)
    main_characters = models.CharField(max_length=200)
    series = models.CharField(max_length=100, blank=True)
    film_adaptation = models.BooleanField(default=False)
    movie_trailer = models.URLField(blank=True)
    tags = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)


    def __str__(self):
        return self.title



