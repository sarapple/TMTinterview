from django.db import models

from interview.core.behaviors import IsActiveModel, TimestampedModel
from interview.inventory.models import Inventory
from django.contrib.auth.hashers import make_password

# Create your models here.
class UserProfile(TimestampedModel, IsActiveModel, models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128) # store hash of password
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField()
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    is_admin = models.BooleanField()
    avatar = models.ImageField()

    def __str__(self) -> str:
        return f'{self.username} - {self.email}'

    def get_full_name() -> str:
      return f'{self.first_name} - {self.last_name}'
    
    def get_username() -> str:
      return self.username
    
    def is_authenticated() -> str:
      raise NotImplementedError()
      # I think this can be done in the view from the request
