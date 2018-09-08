from django import forms



from Rentals.models import Rental

class RentalForm(forms.ModelForm):

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Rental
        fields = ('cost','car')

