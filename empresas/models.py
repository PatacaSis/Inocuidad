from django.db import models

class GrupoTecnologico(models.Model):
    numero = models.CharField(verbose_name='Numero Grupo', max_length=5, unique=True)
    descripcion = models.CharField(verbose_name='Descripcion', max_length=200, unique=True)

    class Meta:
        verbose_name = 'Grupo Tecnologico'
        verbose_name_plural = 'Grupos Tecnologicos'
        ordering = ['numero']    

    def __str__(self):
        return '{} - {}'.format(self.numero,self.descripcion)


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

class Pais(models.Model):
    nombre = models.CharField(verbose_name="Pais exportador", max_length=100)

    class Meta:
        verbose_name = 'Pais exportador'
        verbose_name_plural = 'Paises exportadores'
        ordering = ['nombre']

    def __str__(self):
        return '{}'.format(self.nombre)

class Empresa(models.Model):
    nombre = models.CharField(verbose_name='Razon Social', max_length=50)
    numero = models.CharField(verbose_name='Numero', max_length=20, unique=True)
    localidad = models.CharField(verbose_name='Localidad', max_length=50)
    domicilio = models.CharField(verbose_name='Ubicacion', max_length=50)
    jefe_planta = models.CharField(verbose_name='Jefe de Planta', max_length=100)
    resp_inocuidad = models.CharField(verbose_name='Responsable de inocuidad', max_length=100)
    jefe_servicio_sanitario = models.CharField(verbose_name='Jefe de Servicio Oficial', max_length=100)
    grupos_id = models.ManyToManyField(GrupoTecnologico, verbose_name='Grupos tecnologicos')
    productos_id = models.ManyToManyField(Producto, verbose_name='Productos')
    paises_id = models.ManyToManyField(Pais, verbose_name='Paises habilitados')
    lineas_haccp = models.CharField(verbose_name='Lineas de produccion con HACCP:', max_length=300)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nombre']

    def __str__(self):
        return '{} - {}'.format(self.nombre,self.numero)


class Auditoria(models.Model):
    fecha = models.DateField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    motivo = models.CharField(verbose_name='Motivo de la auditoria', max_length=150)
    criterio = models.CharField(verbose_name='Criterios de auditoria', max_length=250)
    alcance = models.CharField(verbose_name='Alcance de auditoria', max_length=250)
    evidencia = models.TextField(verbose_name='Evidencias encontradas')
    auditores = models.CharField(verbose_name='Auditor/Auditores', max_length=250)
    auditados = models.CharField(verbose_name='Personas de empresa auditada:', max_length=250)
    grupos_id = models.ManyToManyField(GrupoTecnologico, verbose_name='Grupos tecnologicos habilitados')
    nc = models.TextField(verbose_name='No conformidades')
    observaciones = models.TextField(verbose_name='Aclaraciones/Conclusiones')
    estado = models.BooleanField(verbose_name='Abierta/Cerrada', default=False)

    class Meta:
        verbose_name = 'Auditoria'
        verbose_name_plural = 'Auditorias'
        ordering = ['fecha']
    
    def __str__(self):
        return '{}'.format(self.motivo)

TIPO_AGUA = [
    ('Os','Agua de osmosis'),
    ('Po','Agua de pozo'),
    ('Re','Agua de red')
]

TIPO_ANALISIS = [
    ('MB','Microbiologico'),
    ('FQ','Fisicoquimico'),
]

class Agua(models.Model):
    fecha = models.DateField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipo_agua = models.CharField(verbose_name='Fuente de agua ', max_length=2, choices=TIPO_AGUA)
    punto_muestreo = models.CharField(verbose_name='Punto de muestreo', max_length=50)
    tipo_analisis = models.CharField(verbose_name='Tipo de analisis', max_length=2, choices=TIPO_ANALISIS)
    laboratorio = models.CharField(verbose_name='Laboratorio', max_length=50)
    resultado = models.BooleanField(verbose_name='Aceptable/No aceptable')
    observaciones = models.TextField(verbose_name='Observaciones')

    class Meta:
        verbose_name = 'Muestreo de agua'
        verbose_name_plural = 'Muestreos de agua'
        ordering = ['fecha']
    
    def __str__(self):
        return '{}'.format(self.fecha)



     
