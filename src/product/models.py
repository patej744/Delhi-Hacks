from django.db import models

# Create your models here.
class Crop(models.Model):
	# title = models.CharField(max_length=120)
	# desc = models.TextField()
	# price = models.DecimalField(decimal_places = 2,max_digits=5)
    forename = models.CharField(max_length=12)
    surname = models.CharField(max_length=12)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)    
    product = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    quantity = models.IntegerField()
    production_date = models.DateField()
    condition = models.CharField(max_length=9)    
    location = models.CharField(max_length=50)
    desc=models.CharField(max_length=500)

class Machinery(models.Model):
	forename = models.CharField(max_length=12)
	surname = models.CharField(max_length=12)
	email = models.EmailField()
	telephone = models.CharField(max_length=20)    
	product = models.CharField(max_length=50)
	price = models.CharField(max_length=10)
	quantity = models.IntegerField()
	production_date = models.DateField()
	location = models.CharField(max_length=50)
	condition = models.CharField(max_length=9)    
	desc=models.CharField(max_length=500)