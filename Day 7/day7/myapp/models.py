from django.db import models

class Newapp(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    DOB = models.DateField()
    gender = models.CharField(max_length=7)
    nationality = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    pin_code = models.IntegerField()
    qualification = models.CharField(max_length=15)
    salary = models.CharField(max_length=10)
    PAN = models.IntegerField()
