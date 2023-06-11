from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.title
