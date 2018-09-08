# Create your models here.

from django.db import models
from Cars.models import Car

# Create your models here.
class Rental(models.Model):
    car = models.ForeignKey(Car,related_name='car', on_delete=models.CASCADE, null=False)
    startdate=models.DateField(auto_now_add=True)
    enddate = models.DateField(auto_now_add=True)
    cost = models.IntegerField(default=0)


class Meta:
    ordering = ['cost']