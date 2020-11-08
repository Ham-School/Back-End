from django.db import models

# Create your models here.

class Usuario (models.Model):
    apellidoP = models.CharField(max_length=35)
    apellidoM = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    edad = models.PositiveIntegerField()
    tipo = (('Maestro', 'Maestro'), ('Alumno', 'Alumno'))
    Tipo = models.CharField(max_length=7, choices=tipo, default='Alumno')
    fecha = models.DateField()

    def Nombrecompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.apellidoP, self.apellidoM, self.nombre)

    def __str__(self):
        return self.Nombrecompleto()

class Curso (models.Model):
    Usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    clase = models.CharField(max_length=50)
    Grado = models.CharField(max_length=35)

    def __str__(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.Usuario, self.Grado, self.clase)


        
