from django.db import models

# Create your models here.


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()  # This will help us determine if first player made the move
