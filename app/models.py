from django.db import models
from django.urls import reverse


class New(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')
