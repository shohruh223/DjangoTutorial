from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    phone_number = models.CharField(max_length=20)
    confirm = models.PositiveBigIntegerField(null=True, blank=True)
