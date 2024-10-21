from django.db import models

# Create your models here.
class Alumno_T(models.Model):
    nombre=models.CharField(max_length=100,verbose_name='Nombre')
    correo=models.EmailField(max_length=100,verbose_name='Correo electronico')
    class Meta:
        verbose_name="Alumno"
        verbose_name_plural='Alumnos'
        
    def __str__(self):
        return str(self.id)
