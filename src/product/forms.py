from django import forms
class addCropForm(forms.Form):
    forename = forms.CharField(max_length=12)
    surname = forms.CharField(max_length=12)
    email = forms.EmailField()
    telephone = forms.CharField(max_length=20)    
    product = forms.CharField(max_length=50)
    price = forms.DecimalField(decimal_places=2, max_digits=5)
    quantity = forms.IntegerField()
    production_date = forms.DateField()
    condition = forms.CharField(max_length=9)    
    location = forms.CharField(max_length=50)
    desc=forms.CharField(max_length=500)

class addMachineForm(forms.Form):
    forename = forms.CharField(max_length=12)
    surname = forms.CharField(max_length=12)
    email = forms.EmailField()
    telephone = forms.CharField(max_length=20)    
    product = forms.CharField(max_length=50)
    price = forms.DecimalField(decimal_places=2, max_digits=5)
    quantity = forms.IntegerField()
    production_date = forms.DateField()
    location = forms.CharField(max_length=50)
    condition = forms.CharField(max_length=9)    
    desc=forms.CharField(max_length=500)

