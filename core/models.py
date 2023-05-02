from django.db import models

# Create your models here.


class BaseModel(models.Model):
    class Meta:
        abstract = True

    is_deleted = models.BooleanField("Is Deleted", default=False, null=False, blank=False)

# TODO:
class User():
    pass
