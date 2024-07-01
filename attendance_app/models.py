# models.py in attendance_app
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserType(models.Model):
    usertype = models.CharField(max_length=50)

    def __str__(self):
        return self.usertype

    class Meta:
        db_table = 'usertype'

class User(AbstractUser):
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    usertype = models.ForeignKey(UserType, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, blank=True, null=True) 

    class Meta:
        db_table = 'usermaster'
