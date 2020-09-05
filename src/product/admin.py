from django.contrib import admin

# Register your models here.
from .models import Crop, Machinerie

admin.site.register(Crop)
admin.site.register(Machinerie)