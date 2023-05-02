from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DjUserManager
from django.db import models


# Create your models here.


class BaseModel(models.Model):
    class Meta:
        abstract = True

    is_deleted = models.BooleanField("Is Deleted", default=False, null=False, blank=False)


class UserManager(DjUserManager):

    def create_superuser(self, phone, email=None, password=None, **extra_fields):
        return super().create_superuser(phone, email, password, **extra_fields)


class User(AbstractUser):
    phone = models.CharField("Phone", max_length=13, unique=True)
    USERNAME_FIELD = 'phone'

    objects = UserManager()


