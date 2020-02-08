from django.db import models


PRIORITY = (('danger', 'high'), ('infor', 'normal'), ('success', 'low'))
# Create your models here.
# @see https://qiita.com/nachashin/items/f768f0d437e0042dd4b3
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )
    duedate = models.DateField()
    def __str__(self):
        return self.title