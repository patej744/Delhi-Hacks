from django import forms
class addCropForm(forms.Form):
    title=forms.CharField(max_length=120)
    desc=forms.CharField()
    price=forms.DecimalField(decimal_places=2,max_digits=5)

