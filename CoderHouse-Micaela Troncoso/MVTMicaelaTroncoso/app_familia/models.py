from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45, null=True)
    fec_nacimiento = models.DateField(null=True)
    edad = models.IntegerField() 

    def getNombreCompleto(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"