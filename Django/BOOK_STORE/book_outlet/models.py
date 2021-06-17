from django.db import models

# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=100)  # CharField() is a Django Model field type. This shows what kind of
    # data we will store in title field
    rating = models.IntegerField()  # IntegerField() is a Django Model field type. This shows what kind of
    # data we will store in title field

    def __str__(self):
        return f"{self.title} {self.rating}"
