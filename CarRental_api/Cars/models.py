
from django.db import models


# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=100, blank=True, default='')
    model = models.CharField(max_length=100, blank=True, default='')
    year = models.DateField(auto_now_add=True)
    #rentals=models.ForeignKey(Rental, related_name='rentals', on_delete=models.CASCADE, null=False)


    class Meta:
        ordering = ['year']