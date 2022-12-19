from django.db import models
from .estado import estado

# Create your models here.
class Institucion(models.Model):
    institucion = models.CharField(max_length=60)
    
    def __str__(self):
        return self.institucion

class Inscritos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    fechainscripción = models.DateField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    horainscripción = models.TimeField()
    estado = models.CharField(max_length=30, choices=estado)
    observacion = models.CharField(max_length=200, blank=True)
    