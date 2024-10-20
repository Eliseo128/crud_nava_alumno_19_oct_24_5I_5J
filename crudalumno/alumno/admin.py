from django.contrib import admin
from .models import Alumno_T
# Register your models here.

@admin.register(Alumno_T)
class Alumno_TAdmin(admin.ModelAdmin):
    list_display=['id','nombre','correo']