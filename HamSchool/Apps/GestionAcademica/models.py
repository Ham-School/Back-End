from django.db import models

# Create your models here.

class Curso (models.Model):
    clase = models.CharField(max_length=50)
    Grado = models.CharField(max_length=35)

    def Curso (self):
        cadena = "{0}, {1}"
        return cadena.format( self.Grado, self.clase)

    def __str__(self):
        return self.Curso()


class Usuario (models.Model):
    apellidoP = models.CharField(max_length=35)
    apellidoM = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    edad = models.PositiveIntegerField()
    tipo = (('Maestro', 'Maestro'), ('Alumno', 'Alumno'))
    Tipo = models.CharField(max_length=7, choices=tipo, default='Alumno')
    fecha = models.DateField(auto_now_add=True)
    mail = models.CharField(max_length=50)


    def Nombrecompleto(self):
        cadena = "{0} {1} {2} {3} "
        return cadena.format(self.Tipo,self.nombre, self.apellidoP, self.apellidoM)

    def __str__(self):
        return self.Nombrecompleto()





        
