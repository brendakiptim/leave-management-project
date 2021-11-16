from django.db import models

# Create your models here.
class Leave(models.Model):
    name = models.CharField(max_length=15)
    days= models.IntegerField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name