from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.urls import reverse


    
class User(AbstractUser):

    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(null=True, blank=True, max_length=50)
    field_of_study = models.CharField(null=True, blank=True, max_length=100)


    class Meta:
        db_table = "User"