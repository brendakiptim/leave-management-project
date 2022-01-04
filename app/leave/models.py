from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core import validators
# Create your models here.
# create Leave db model
class Leave(models.Model):
    name = models.CharField(max_length=15)
    days= models.IntegerField(default=21)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# create employee db model
class Employee(models.Model):
    first_name= models.CharField(blank=False, max_length=30)
    last_name= models.CharField(blank=False, max_length=30)
    leave_days = models.IntegerField(default=21, validators=[
            MaxValueValidator(21),
            MinValueValidator(0)
        ])
    remaining_leave_days = models.IntegerField(default=21, validators=[
            MaxValueValidator(21),
            MinValueValidator(0)
        ])
    used_leave_days = models.IntegerField(default=0,validators=[
            MaxValueValidator(21),
            MinValueValidator(0)
        ])
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'