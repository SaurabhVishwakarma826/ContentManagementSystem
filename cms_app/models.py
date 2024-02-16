from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=False, default='')
    phone = models.CharField(max_length=10, blank=False, default='')
    address = models.TextField(blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    pincode = models.CharField(max_length=6, blank=False, default='')

    def __str__(self):
        return self.username

class Content(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=False)
    body = models.TextField(max_length=300, blank=False)
    summary = models.CharField(max_length=60, blank=False)
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    categories = models.ManyToManyField('Category', related_name='contents')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name