from django.db import models
from django.core.validators import validate_email,RegexValidator
from django.contrib.auth.models import AbstractUser, Group, Permission
from .managers import Users_INFOManager
from django.contrib.auth.models import AbstractUser
import random
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password


# Create your models here.
class CustomAutoField(models.AutoField):
    def __init__(self, *args, **kwargs):
        kwargs['editable'] = False
        super().__init__(*args, **kwargs)


class Users_INFO(AbstractUser):
    username=None
    u_id=CustomAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    college = models.CharField("college name", max_length=50)
    phoneNO = models.CharField(max_length=10, validators=[
        RegexValidator(regex=r'^\d{10,15}$', message='Phone number must be between 10 and 15 digits.'),
    ])
    # Add any additional fields you need
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = Users_INFOManager()

    def save(self, *args, **kwargs):   #this is save overide funcion which is called when we save the model 
        if not self.u_id:
            if self.phoneNO:
                # Use the last 4 digits of the phone number if available
                u_id = int(self.phoneNO[-4:])
            else:
                # Generate a random 4-digit number
                u_id = random.randint(1000, 9999)      #################

            self.u_id = u_id
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.u_id)
        