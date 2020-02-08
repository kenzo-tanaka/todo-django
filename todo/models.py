from django.db import models

# Create your models here.
# @see https://qiita.com/nachashin/items/f768f0d437e0042dd4b3
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()