from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.TextField()
