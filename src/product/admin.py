from django.contrib import admin

# Register your models here.
from .models import Crop, Machinery

admin.site.register(Crop)
admin.site.register(Machinery)