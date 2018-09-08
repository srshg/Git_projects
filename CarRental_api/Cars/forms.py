from django import forms



from Cars.models import Car

class CarForm(forms.ModelForm):
    #brand=forms.CharField(max_length=128,help_text="Brand")
    #model=forms.CharField(max_length=128,help_text="Model")
    #year=forms.DateField(help_text="Year")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Car
        fields = ('brand', 'model')
