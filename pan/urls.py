# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'panaderia.views.home', name='home'),
    # url(r'^pan/', include('pan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    # my urls
    url(r'^login/$', 'panaderia.views.ingreso'),
    url(r'^logout/$', 'panaderia.views.salida'),
    url(r'^operaciones/$', 'panaderia.views.operaciones'),
    url(r'^operaciones/change_password/$', 'panaderia.views.change_password'),
    url(r'^almacen/$', 'panaderia.views.almacen'),
    url(r'^stock_actual/$', 'panaderia.views.stock_actual'),
    url(r'^tipos_de_pan/$', 'panaderia.views.tipos_pan'),
    url(r'^tipos_de_pan/editar/(?P<codigo>\d+)/$', 'panaderia.views.tipos_pan_editar'),
    url(r'^tipos_de_pan/nuevo/$', 'panaderia.views.tipos_pan_nuevo'),
    url(r'^egreso/$', 'panaderia.views.egreso'),
    url(r'^produccion/$', 'panaderia.views.admin_produccion'),
    url(r'^ventas/$', 'panaderia.views.ventas'),
    url(r'^ventas/venta/$', 'panaderia.views.venta'),
    url(r'^ventas/venta/grupal/(?P<id_cliente>\d+)/$', 'panaderia.views.venta_grupal'),
    url(r'^ventas/deudores/$', 'panaderia.views.deudores'),
    url(r'^ventas/deudores/(?P<codigo>\d+)/$', 'panaderia.views.deudores_cliente'),
    url(r'^ventas/pagar/(?P<codigo>\d+)/$', 'panaderia.views.pagar'),
    url(r'^ventas/devolucion/$', 'panaderia.views.devolucion'),
    url(r'^ventas/devolucion/grupal/(?P<id_cliente>\d+)/$', 'panaderia.views.devolucion_grupal'),
    url(r'^reporte/$', 'panaderia.views.reporte'),
    url(r'^reporte/ingresos/$', 'panaderia.views.reporte_ingresos'),
    url(r'^reporte/ingresos/hoy/$', 'panaderia.views.reporte_hoy_ingresos'),
    url(r'^reporte/ventas/$', 'panaderia.views.reporte_ventas'),
    url(r'^reporte/general/$', 'panaderia.views.reporte_general'),
    url(r'^reporte/egresos/$', 'panaderia.views.reporte_egresos'),
    url(r'^reporte/ganancias/$', 'panaderia.views.reporte_ganancias'),
    url(r'^datos_pan/(?P<codigo>\w+)/$', 'panaderia.views.datos_pan'),
    url(r'^datos_deuda/(?P<id_pan>\w+)/(?P<id_cliente>\w+)/$', 'panaderia.views.datos_deuda'),
    url(r'^eliminar/(?P<codigo>\w+)/$', 'panaderia.views.eliminar_venta'),
    url(r'^eliminar/egreso/(?P<codigo>\w+)/$', 'panaderia.views.eliminar_egreso'),
    url(r'^modificar/(?P<codigo>\d+)/$', 'panaderia.views.modificar_venta'),
)
