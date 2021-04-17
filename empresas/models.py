from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(verbose_name='Razon Social', max_length=50)
    numero = models.CharField(verbose_name='Identificacion', max_length=20, unique=True)
    localidad = models.CharField(verbose_name='Localidad', max_length=50)
    domicilio = models.CharField(verbose_name='Ubicacion', max_length=50)
    productos = models.CharField(verbose_name='Productos', max_length=50)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nombre']

    def __str__(self):
        return '{} - {}'.format(self.nombre,self.numero)
     
