from django.db import models


class User(models.Model):
    image = models.ImageField(upload_to='user/%Y/%m/%d')
    fullname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.fullname

