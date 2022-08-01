from pyexpat import model
from sre_constants import MAX_UNTIL
from django.db import models

# Create your models here.
class RegisterUser(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, unique=True)
    password = models.CharField(max_length=10)
    # mobileNo = models.PhoneNumberField()
    address = models.TextField(max_length=200)
    class Meta:
        db_table = "RegisterUser"

