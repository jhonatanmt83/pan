# -*- coding: utf-8 -*-
from django.contrib import admin
from panaderia.models import TipoAlmacen, TipoPan, Producion, Cliente, Ingreso, Venta, Deuda, Pago, Egreso, Devolucion

#admin.site.register(TipoCantidad)
admin.site.register(TipoAlmacen)
admin.site.register(TipoPan)
admin.site.register(Producion)
admin.site.register(Cliente)
admin.site.register(Ingreso)
admin.site.register(Venta)
admin.site.register(Deuda)
admin.site.register(Pago)
admin.site.register(Egreso)
admin.site.register(Devolucion)
