from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=100)  # CharField() is a Django Model field type. This shows what kind of
    # data we will store in title field
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # IntegerField() is a Django Model field type. This shows what kind of
    # data we will store in title field. We have added the validators as a Keyword arg by importing
    # the validators class and instantiating the Min and MaxValueValidator
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)  # Harry Potter 1 => harry-potter-1

    def get_absolute_url(self):  # We are overriding this method which automatically gets called by Django to load
        # the specific url/page
        return reverse("book-detail", args=[self.slug])

    # Here we are overwriting the save() method and slugifying the title of the book
    # This slugified field will be then used in the URLs
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super(Book, self).save()

    def __str__(self):
        return f"{self.title} {self.rating}"
