from django.db import models
from django.utils.text import slugify

# Create your models here.

CATEGORY_BOOKS = {
    ("fantasty", "FANTASY"),
    ("sci_fi", "SCI_FI"),
    ("horror", "HORROR"),
    ("biographies", "BIOGRAPHIES"),
    ("romance", "ROMANCE"),
    ("thrillers", "THRILLERS"),
}

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books')
    data_of_production = models.DateField()
    category = category = models.CharField(choices=CATEGORY_BOOKS, max_length=15)
    description = models.TextField(max_length=1000)
    main_characters = models.CharField(max_length=200)
    name_series = models.CharField(max_length=100, blank=True)
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
        return self.title+ " - " + str(self.author)

"""- Tytuł
-autor
- data wydania
- zdjęcie okładki
- kategoria
- opis
-bohaterowie
- cykl
-adaptacja filmowa 
- link do trailera
- tags
"""