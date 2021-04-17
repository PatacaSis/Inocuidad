from django.db import models

class TematicaDocumental(models.Model):
    titulo = models.CharField(max_length=50, unique=True)
    texto = models.CharField(max_length=150, blank=True, null=True)
    imagen = models.ImageField(upload_to='principal')

    class Meta:
        verbose_name = 'Clasificacion de norma'
        verbose_name_plural = 'Clasificacion de normas'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


TIPO_NORMA_CHOICES = [
    
    ('CIRCULAR','Circular'),
    ('CAA','Codigo Alimentario Argentino'),
    ('MEMORANDUN','Memorandun'),
    ('ORDEN SERVICIO','Orden de Servicio'),
    ('R80','Resol 80/96 - GMC'),
]

class temasNormas(models.Model):
    tema = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Tema de norma'
        verbose_name_plural = 'Tema de normas'
        ordering = ['tema']

    def __str__(self):
        return self.tema


class Normativa(models.Model):
    fecha = models.DateField(verbose_name='Fecha del documento',  blank=True, null=True)
    tipo = models.CharField(verbose_name='Tipo de norma', max_length=10, choices=TIPO_NORMA_CHOICES)
    tema = models.ForeignKey(temasNormas, on_delete=models.CASCADE)
    numero = models.CharField(verbose_name='Numero del documento', max_length=10, blank=True, null=True)
    titulo = models.CharField(verbose_name='Titulo de documento', max_length=100, blank=True, null=True)
    texto = models.FileField(upload_to='normativas', blank=True, null=True)
    pais = models.CharField(verbose_name='Pais a exportar', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Normativa'
        verbose_name_plural = 'Normativas'
        ordering = ['tipo','fecha']

    def __str__(self):
        return '{} - {}'.format(self.tipo,self.tema)


TIPO_ALIMENTO_CHOICES = [
    ('Lacteos','Lacteos'),
    ('Miel','Miel')
]

class Alimento(models.Model):
    tipo = models.CharField(verbose_name='Tipo de alimento', max_length=8, choices=TIPO_ALIMENTO_CHOICES)
    nombre = models.CharField(max_length=150)
    caa = models.CharField(verbose_name='Articulo del CAA', max_length=50, null=True, blank=True)
    norma = models.FileField(upload_to='normas_Alimentos', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class CodAliArg(models.Model):
    cap = models.CharField(verbose_name='Capitulo', max_length=15, unique=True)
    titulo = models.CharField(verbose_name='Titulo', max_length=100, unique=True)
    texto = models.FileField(verbose_name='Texto', upload_to='CAA')

    class Meta:
        verbose_name = 'Codigo Alimentario Argentino'
        verbose_name_plural = 'Codigo Alimentario Argentino'

    def __str__(self):
        return '{} - {}'.format(self.cap,self.titulo)


class Codex(models.Model):
    identifi = models.CharField(verbose_name='Identificacion de la norma', max_length=100, unique=True)
    texto = models.FileField(verbose_name='Texto', upload_to='Codex')

    class Meta:
        verbose_name = 'Codex Alimentarius'
        verbose_name_plural = 'Codex Alimentarius'

    def __str__(self):
        return self.identifi
    