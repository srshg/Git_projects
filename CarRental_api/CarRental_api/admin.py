
from django.contrib import admin

from Cars.models import Car
from Rentals.models import Rental

admin.site.register(Car)
admin.site.register(Rental)

