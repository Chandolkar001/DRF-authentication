from tkinter.messagebox import NO
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone_no = models.CharField(max_length=10)
    REQUIRED_FIELDS = ['username', 'phone_no', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

