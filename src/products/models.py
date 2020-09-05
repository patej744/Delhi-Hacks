from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(maxlength=50)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2)
    img         = models.ImageField()