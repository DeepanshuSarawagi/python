from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=100)  # CharField() is a Django Model field type. This shows what kind of
    # data we will store in title field
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # IntegerField() is a Django Model field type. This shows what kind of
    # data we will store in title field. We have added the validators as a Keyword arg by importing
    # the validators class and instantiating the Min and MaxValueValidator
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} {self.rating}"
