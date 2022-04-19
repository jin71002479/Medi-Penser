from django.db import models
from django.contrib.auth.models import AbstractUser
# from phonenumber_field.modelfields import PhoneNumberField
# from django.core.validators import RegexValidator

class User(AbstractUser):

    fullname = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    parmacy = models.CharField(max_length=50)
    relation = models.CharField(max_length=80, null=True)
    phone = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)