# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class TipoAlmacen(models.Model):
    class Meta:
        verbose_name = ('TipoAlmacen')
        verbose_name_plural = ('TipoAlmacenes')

    nombre = models.CharField(max_length=50, verbose_name='Nombre')

    def __unicode__(self):
        return self.nombre


class TipoPan(models.Model):
    class Meta:
        verbose_name = ('TipoPan')
        verbose_name_plural = ('TipoPanes')

    nombre = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    tipoalmacen = models.ForeignKey(TipoAlmacen, verbose_name='Tipo')
    precio = models.DecimalField(max_digits=8, decimal_places=3, verbose_name='Precio S/.')
    grupo = models.IntegerField(verbose_name='Grupo de', blank=True, null=True)

    def __unicode__(self):
        return self.nombre


class Producion(models.Model):
    class Meta:
        verbose_name = ('Producion')
        verbose_name_plural = ('Produciones')
        ordering = ['tipopan']

    tipopan = models.OneToOneField(TipoPan, verbose_name='Tipo de Pan', primary_key=True)
    stock = models.IntegerField(verbose_name='Stock')

    def __unicode__(self):
        return str(self.tipopan) + " => " + str(self.stock)


class Cliente(models.Model):
    class Meta:
        verbose_name = ('Cliente')
        verbose_name_plural = ('Clientes')

    nombre = models.CharField(max_length=50, verbose_name='Nombre')

    def __unicode__(self):
        return self.nombre


class Ingreso(models.Model):
    class Meta:
        verbose_name = ('Ingreso')
        verbose_name_plural = ('Ingresos')

    tipopan = models.ForeignKey(TipoPan, verbose_name='Tipo de Pan')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.tipopan) + " => " + str(self.cantidad)


class Venta(models.Model):
    class Meta:
        verbose_name = ('Venta')
        verbose_name_plural = ('Ventas')

    tipopan = models.ForeignKey(TipoPan, verbose_name='Tipo de Pan', related_name='tipo_pan_venta')
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', related_name='cliente_venta')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.tipopan) + " => " + str(self.cliente) + " => " + str(self.cantidad) + " => " + str(self.fecha)

    def precio(self):
        return self.cantidad * self.tipopan.precio


class Deuda(models.Model):
    class Meta:
        verbose_name = ('Deuda')
        verbose_name_plural = ('Deudas')

    tipopan = models.ForeignKey(TipoPan, verbose_name='Tipo de Pan', related_name='tipo_pan_deuda')
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', related_name='cliente_deuda')
    monto = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Monto S/.')
    cancelado = models.BooleanField(verbose_name='Cancelado')

    def __unicode__(self):
        return str(self.tipopan) + " => " + str(self.cliente) + " => " + str(self.monto) + " => " + str(self.cancelado)

    def monto_punto(self):
        cad = str(self.monto)
        return cad.replace(',', '.')


class Pago(models.Model):
    class Meta:
        verbose_name = ('Pago')
        verbose_name_plural = ('Pagos')

    deuda = models.ForeignKey(Deuda, verbose_name='Deuda', related_name='deuda_pago')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total S/.')
    monto = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Monto S/.')
    restante = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Restante S/.')
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.deuda) + " => " + str(self.monto) + " => " + str(self.fecha)


class Egreso(models.Model):
    class Meta:
        verbose_name = ('Egreso')
        verbose_name_plural = ('Egresos')

    monto = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Monto S/.')
    descripcion = models.TextField(verbose_name='Descripcion')
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        pass


class Devolucion(models.Model):
    class Meta:
        verbose_name = ('Devolucion')
        verbose_name_plural = ('Devoluciones')

    tipopan = models.ForeignKey(TipoPan, verbose_name='Tipo de Pan', related_name='tipo_pan_devolucion')
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', related_name='cliente_devolucion')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    #descripcion = models.TextField(verbose_name='Descripcion', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.tipopan) + " => " + str(self.cliente) + " => " + str(self.cantidad) + " => " + str(self.fecha)
