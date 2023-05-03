from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DjUserManager
from django.db import models


# Create your models here.


class BaseModel(models.Model):
    class Meta:
        abstract = True

    is_deleted = models.BooleanField("Is Deleted", default=False, null=False, blank=False)
    last_change = models.DateTimeField(auto_now=True)
    create_datetime = models.DateTimeField(auto_created=True)
    delete_datetime = models.DateTimeField(default=None, null=True, blank=True)


class UserManager(DjUserManager):

    def create_superuser(self, phone, email=None, password=None, **extra_fields):
        extra_fields['phone'] = phone
        return super().create_superuser(phone, email, password, **extra_fields)


class User(AbstractUser):
    phone = models.CharField("Phone", max_length=13, unique=True)
    USERNAME_FIELD = 'phone'

    objects = UserManager()


class Student(User):
    class Meta:
        permissions = [("view_student_exams", "Can view students exam")]

    student_id = models.CharField("Student id", max_length=20)
    age = models.IntegerField("Age")
