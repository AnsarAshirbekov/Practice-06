from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    published_date = models.DateField(default = "2000-01-01")
    pages = models.IntegerField(default=0, null=False)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=100, blank = True)
    price = models.DecimalField(max_digits = 10, decimal_places=2, default = 0)
    rating = models.DecimalField(max_digits = 10, decimal_places=2, null = True)


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank = True)
    text = models.TextField(blank=True)
    published_date = models.DateTimeField(auto_now_add = True)

