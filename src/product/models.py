from django.db import models

# Create your models here.
class Crop(models.Model):
	title = models.CharField(max_length=120)
	desc = models.TextField()
	price = models.DecimalField(decimal_places = 2,max_digits=5)

class Machinerie(models.Model):
	title = models.TextField()
	desc = models.TextField()
	price = models.TextField()
	image = models.TextField(default="image")
	location = models.TextField(default="ye")
	condition = models.TextField(default="ye")