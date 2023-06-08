from django.db import models


class User(models.Model):
    image = models.ImageField(upload_to='picture/')
    fullname = models.CharField(max_length=55)
    job = models.CharField(max_length=55)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname

