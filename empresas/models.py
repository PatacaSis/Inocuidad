from django.db import models

class Producto(models.Model):
    tipo = models.CharField(verbose_name='Tipo producto', max_length=100)
    nombre = models.CharField(verbose_name='Nombre producto', max_length=100)
    codigo = models.CharField(verbose_name='Codigo', max_length=100)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['tipo']

    def __str__(self):
        return '{}'.format(self.tipo)

class Empresa(models.Model):
    nombre = models.CharField(verbose_name='Razon Social', max_length=50)
    numero = models.CharField(verbose_name='Numero', max_length=20, unique=True)
    localidad = models.CharField(verbose_name='Localidad', max_length=50)
    domicilio = models.CharField(verbose_name='Ubicacion', max_length=50)
    productos_id = models.ManyToManyField(Producto)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nombre']

    def __str__(self):
        return '{} - {}'.format(self.nombre,self.numero)
     
