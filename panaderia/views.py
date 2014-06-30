# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import json
import datetime
from django.db.models import Sum
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
#formularios
from panaderia.forms import IngresoForm, formingreso, BaseIngresoFormSet, TipoPanForm,  FechaForm
from panaderia.forms import EgresoForm, TipoPanSelect, VentaForm, PagoForm, FechasForm
from panaderia.forms import ClienteSeleccionForm, DevolucionForm, VentaForm_s, BaseVentaFormSet
from panaderia.forms import DevolucionForm_g, BaseDevolucionFormSet, formpassword
#modelos de pan
from panaderia.models import *


#@login_required
def home(request):
    # codigo
    return render_to_response('index.html', {}, context_instance=RequestContext(request))


def ingreso(request):
    error = ''
    mensaje = ''
    if request.method == 'POST':
        formu = formingreso(request.POST)
        usuariologin = request.POST['usuarioform']
        passlogin = request.POST['passform']
        acceso = authenticate(username=usuariologin, password=passlogin)
        if acceso is not None:
            if acceso.is_active:
                login(request, acceso)
                try:
                    url_next = request.GET['next']
                    if len(url_next) > 0:
                        return HttpResponseRedirect(url_next)
                except:
                    pass
                return HttpResponseRedirect('/')
            else:
                error = 'yes'
                mensaje = 'El usuario no esta activo.'
        else:
            error = 'yes'
            mensaje = 'Usuario y/o contraseña incorrectos. Intente nuevamente.'
    else:
        formu = formingreso()
    return render_to_response('login.html', {'formu': formu, 'msg': mensaje, 'error': error}, context_instance=RequestContext(request))


@login_required
def change_password(request):
    error = ''
    mensaje = ''
    if request.method == 'POST':
        formu = formpassword(request.POST)
        pass1 = request.POST['passform1']
        pass2 = request.POST['passform2']
        if pass1 == pass2:
            usuario = request.user
            usuario.set_password(pass1)
            usuario.save()
            return HttpResponseRedirect('/operaciones/')
        else:
            error = 'yes'
            mensaje = 'Las contraseñas deben ser las mismas. Intente nuevamente.'
    else:
        formu = formpassword()
    return render_to_response('change_password.html', {'formu': formu, 'msg': mensaje, 'error': error}, context_instance=RequestContext(request))


#@login_required()
def salida(request):
    logout(request)
    return render_to_response('logout.html')


@login_required
def operaciones(request):
    return render_to_response('operaciones.html', {}, context_instance=RequestContext(request))


@login_required
def almacen(request):
    contador_guardados = 0
    guardados = []
    ingre_total = len(TipoPan.objects.all())
    IngresoFormSet = formset_factory(IngresoForm, formset=BaseIngresoFormSet, max_num=ingre_total)
    inicial = conteos()
    if request.method == 'POST':
        enviar = IngresoFormSet(request.POST)
        for x in enviar:
            if x.is_valid():
                input_cantidad = x.__getitem__('cantidad')
                try:
                    input_cantidad = str(input_cantidad).split('value="')[1].split('"')[0]
                    if int(input_cantidad) > 0:
                        guardado = x.save()
                        try:
                            produ = Producion.objects.get(pk=guardado.tipopan)
                            produ_mod = produ
                            #print produ_mod.stock + guardado.cantidad
                            produ_mod.stock = produ_mod.stock + guardado.cantidad
                            produ_mod.save()
                            guardados.append({'tipo': guardado.tipopan, 'cantidad': guardado.cantidad})
                        except:
                            produ_mod = Producion(tipopan=guardado.tipopan, stock=guardado.cantidad)
                            produ_mod.save()
                        contador_guardados += 1
                except:
                    pass
            else:
                pass
    else:
        enviar = IngresoFormSet(initial=inicial)
    if contador_guardados > 0:
        inicial = conteos()
        enviar = IngresoFormSet(initial=inicial)
    return render_to_response('almacen.html', {'formset': enviar, 'guardados': contador_guardados, 'guardados_list': guardados}, context_instance=RequestContext(request))


@login_required
def stock_actual(request):
    producciones = Producion.objects.all()
    return render_to_response('stock_actual.html', {'producciones': producciones}, context_instance=RequestContext(request))


@login_required
def tipos_pan(request):
    tipos = TipoPan.objects.all()
    return render_to_response('tipos_pan.html', {'tipos': tipos}, context_instance=RequestContext(request))


@login_required
def tipos_pan_editar(request, codigo):
    tipo = TipoPan.objects.get(pk=codigo)
    if request.method == 'POST':
        formu = TipoPanForm(request.POST, instance=tipo)
        if formu.is_valid():
            formu.save()
            return HttpResponseRedirect('/tipos_de_pan/')
    else:
        formu = TipoPanForm(instance=tipo)
    return render_to_response('tipos_pan_editar.html', {'formu': formu}, context_instance=RequestContext(request))


@login_required
def tipos_pan_nuevo(request):
    if request.method == 'POST':
        formu = TipoPanForm(request.POST)
        if formu.is_valid():
            guardado = formu.save()
            new_produ = Producion(tipopan=guardado, stock=0)
            new_produ.save()
            return HttpResponseRedirect('/tipos_de_pan/')
    else:
        formu = TipoPanForm()
    return render_to_response('tipos_pan_nuevo.html', {'formu': formu}, context_instance=RequestContext(request))


@login_required
def egreso(request):
    mensaje = ''
    if request.method == 'POST':
        formu = EgresoForm(request.POST)
        if formu.is_valid():
            formu.save()
            mensaje = 'Agregado correctamente.'
            formu = EgresoForm()
    else:
        formu = EgresoForm()
    return render_to_response('egreso.html', {'formu': formu, 'mensaje': mensaje}, context_instance=RequestContext(request))


@login_required
def admin_produccion(request):
    if request.user.is_staff:
        produ_total = len(Producion.objects.all())
        ProduccionFormSet = modelformset_factory(Producion, max_num=produ_total)
        if request.method == "POST":
            formset = ProduccionFormSet(request.POST, request.FILES,
                                    queryset=Producion.objects.order_by('pk'))
            if formset.is_valid():
                formset.save()
        else:
            formset = ProduccionFormSet(queryset=Producion.objects.order_by('pk'))
        return render_to_response('admin_produccion.html', {'formset': formset}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


@login_required
def ventas(request):
    # codigo
    return render_to_response('ventas.html', {}, context_instance=RequestContext(request))


@login_required
def reporte(request):
    # codigo
    return render_to_response('reportes.html', {}, context_instance=RequestContext(request))


@login_required
def reporte_ingresos(request):
    fecha_ini = ''
    fecha_fin = ''
    fechaform = FechaForm
    consultado = 'no'
    devolver = []
    form_panes = TipoPanSelect()
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']
    tipo_pan = ''
    totales = {'unidades': 0, 'importe': 0}
    if request.method == 'POST' and request.POST['tipopan'] != '':
        a = datetime.date.today()
        fecha_hoy = datetime.datetime(a.year, a.month, a.day)
        try:
            fecha = request.POST['fecha'].split('/')
            dia = int(fecha[0])
            mes = int(fecha[1])
            anio = int(fecha[2])
            fecha_hoy = datetime.datetime(anio, mes, dia)
        except:
            a = datetime.date.today()
            fecha_hoy = datetime.datetime(a.year, a.month, a.day)
        consultado = 'si'
        tipo_pan = TipoPan.objects.get(pk=request.POST['tipopan'])
        fecha_ini = fecha_hoy - datetime.timedelta(days=fecha_hoy.weekday())
        fecha_fin = fecha_hoy + datetime.timedelta(days=6 - fecha_hoy.weekday())
        ingresos = Ingreso.objects.filter(fecha__lt=fecha_fin, fecha__gte=fecha_ini, tipopan=tipo_pan)
        for dia in range(2, 8):
            ingreso_a = ingresos.filter(fecha__week_day=dia)
            unidades = 0
            importe = 0
            unidad = ''
            for ingreso in ingreso_a:
                unidades += ingreso.cantidad
            importe = tipo_pan.precio * unidades
            if tipo_pan.tipoalmacen.pk == 1:
                unidad = 'bolsa'
            else:
                unidad = 'pan'
            agregar = {'dia': dias[dia - 2], 'unidades': unidades, 'importe': importe, 'unidad': unidad}
            totales['unidades'] += unidades
            totales['importe'] += importe
            devolver.append(agregar)
    return render_to_response('reporte_ingresos.html', {'devolver': devolver, 'consultado': consultado, 'formulario': form_panes, 'tipo_pan': tipo_pan, 'totales': totales, 'fechaform': fechaform, 'fecha_ini': fecha_ini, 'fecha_fin': fecha_fin}, context_instance=RequestContext(request))


@login_required
def reporte_hoy_ingresos(request):
    fecha = datetime.datetime.now()
    anio = fecha.year
    mes = fecha.month
    dia = fecha.day
    ingresos = Ingreso.objects.filter(fecha__year=anio, fecha__month=mes, fecha__day=dia)
    return render_to_response('reporte_hoy_ingresos.html', {'ingresos': ingresos}, context_instance=RequestContext(request))


@login_required
def reporte_ventas(request):
    fecha = datetime.datetime.now()
    anio = fecha.year
    mes = fecha.month
    dia = fecha.day
    consultado = 'no'
    reportes = []
    clientes = Cliente.objects.all()
    fechaform = FechaForm
    if request.method == 'POST':
        consultado = 'si'
        try:
            fecha = request.POST['fecha'].split('/')
            dia = int(fecha[0])
            mes = int(fecha[1])
            anio = int(fecha[2])
            fecha = datetime.datetime(anio, mes, dia)
        except:
            fecha = datetime.datetime.now()
            anio = fecha.year
            mes = fecha.month
            dia = fecha.day
        if request.POST['cliente'] == 'todos':
            reportes = Venta.objects.filter(fecha__year=anio, fecha__month=mes, fecha__day=dia)
        else:
            cliente = Cliente.objects.get(pk=request.POST['cliente'])
            reportes = Venta.objects.filter(fecha__year=anio, fecha__month=mes, fecha__day=dia, cliente=cliente)
        if len(reportes) > 0:
            reportes = reportes.order_by('cliente')
    return render_to_response('reporte_ventas.html', {'clientes': clientes, 'consultado': consultado, 'reportes': reportes, 'fechaform': fechaform, 'fecha': fecha}, context_instance=RequestContext(request))


@login_required
def reporte_general(request):
    devolver = ''
    fechaform = FechaForm
    fecha_hoy = True
    if request.method == 'POST':
        try:
            fecha = request.POST['fecha'].split('/')
            dia = int(fecha[0])
            mes = int(fecha[1])
            anio = int(fecha[2])
            fecha = datetime.datetime(anio, mes, dia)
            fecha_hoy = False
        except:
            fecha = datetime.datetime.now()
            anio = fecha.year
            mes = fecha.month
            dia = fecha.day
    if fecha_hoy:
        fecha = datetime.datetime.now()
        anio = fecha.year
        mes = fecha.month
        dia = fecha.day
    tipos = TipoPan.objects.all()
    clientes = Cliente.objects.all()
    devolver = []
    for tipo in tipos:
        total_ventas = 0
        saldo_inicial = 0
        saldo = 0
        saldo_final = 0
        total_ingresos = 0
        add_clientes = []
        for cliente in clientes:
            ventas = Venta.objects.filter(tipopan=tipo, cliente=cliente, fecha__year=anio, fecha__month=mes, fecha__day=dia)
            total = 0
            if len(ventas) > 0:
                total = ventas.aggregate(total=Sum('cantidad'))
                add_clientes.append(total['total'])
            else:
                add_clientes.append('-')
        #para el saldo inicial y final
        produ = Producion.objects.get(pk=tipo)
        vendidos = Venta.objects.filter(tipopan=tipo, fecha__year=anio, fecha__month=mes, fecha__day=dia)
        if vendidos:
            total_ventas = vendidos.aggregate(total=Sum('cantidad'))
            total_ventas = total_ventas['total']
        ingresos = Ingreso.objects.filter(tipopan=tipo, fecha__year=anio, fecha__month=mes, fecha__day=dia)
        if ingresos:
            total_ingresos = ingresos.aggregate(total=Sum('cantidad'))
            total_ingresos = total_ingresos['total']
        saldo_inicial = produ.stock + total_ventas - total_ingresos
        saldo_final = produ.stock
        ingreso = total_ingresos
        saldo = saldo_inicial - total_ventas
        devolver.append({'tipo': tipo, 'ventas': add_clientes, 'saldo_inicial': saldo_inicial, 'saldo_final': saldo_final, 'ingreso': ingreso, 'saldo': saldo, 'total_ventas': total_ventas})
    return render_to_response('reporte_general.html', {'clientes': clientes, 'devolver': devolver, 'fecha': fecha, 'fechaform': fechaform}, context_instance=RequestContext(request))


@login_required
def reporte_egresos(request):
    egresos = ''
    total = 0
    fecha_ini = ''
    fecha_fin = ''
    formulario = FechasForm
    if request.method == 'POST':
        try:
            lista_fecha1 = request.POST['fecha1'].split('/')
            fecha_ini = datetime.datetime(int(lista_fecha1[2]), int(lista_fecha1[1]), int(lista_fecha1[0]))
            lista_fecha2 = request.POST['fecha2'].split('/')
            fecha_fin = datetime.datetime(int(lista_fecha2[2]), int(lista_fecha2[1]), int(lista_fecha2[0]) + 1)
            egresos = Egreso.objects.filter(fecha__lte=fecha_fin, fecha__gte=fecha_ini)
        except:
            egresos = Egreso.objects.all()
    else:
        egresos = Egreso.objects.all()
    total = egresos.aggregate(total=Sum('monto'))
    if total['total']:
        total = total['total']
    else:
        total = "0.00"
    return render_to_response('reporte_egresos.html', {'egresos': egresos, 'formulario': formulario, 'total': total, 'fecha_ini': fecha_ini, 'fecha_fin': fecha_fin, }, context_instance=RequestContext(request))


@login_required
def reporte_ganancias(request):
    egresos = ''
    formulario = FechasForm
    datos = []
    fecha_ini = ''
    fecha_fin = ''
    total_e = 0
    totales = {'ingresos': 0, 'ventas': 0, 'devoluciones': 0, 'resta': 0, 'pagado': 0, 'produccion': 0, 'ganancia': 0, 'ganancia_neta': 0}
    if request.method == 'POST':
        lista_fecha1 = request.POST['fecha1'].split('/')
        fecha_ini = datetime.datetime(int(lista_fecha1[2]), int(lista_fecha1[1]), int(lista_fecha1[0]))
        lista_fecha2 = request.POST['fecha2'].split('/')
        fecha_fin = datetime.datetime(int(lista_fecha2[2]), int(lista_fecha2[1]), int(lista_fecha2[0]) + 1)
        tipos = TipoPan.objects.all()
        for tipo in tipos:
            ingresos = Ingreso.objects.filter(tipopan=tipo, fecha__lte=fecha_fin, fecha__gte=fecha_ini)
            total_ing = ingresos.aggregate(total=Sum('cantidad'))
            try:
                total_i = total_ing['total'] * tipo.precio
            except:
                total_i = 0
            devoluciones = Devolucion.objects.filter(tipopan=tipo, fecha__lte=fecha_fin, fecha__gte=fecha_ini)
            total_devo = devoluciones.aggregate(total=Sum('cantidad'))
            try:
                total_d = total_devo['total'] * tipo.precio
            except:
                total_d = 0
            ventas = Venta.objects.filter(tipopan=tipo, fecha__lte=fecha_fin, fecha__gte=fecha_ini)
            total_vent = ventas.aggregate(total=Sum('cantidad'))
            try:
                total_v = total_vent['total'] * tipo.precio
            except:
                total_v = 0
            pagos = Pago.objects.filter(deuda__tipopan=tipo, fecha__lte=fecha_fin, fecha__gte=fecha_ini)
            total_pag = pagos.aggregate(total=Sum('monto'))
            if len(pagos) >= 1:
                total_p = total_pag['total']
            else:
                total_p = 0
            resta = total_v - total_d - total_p
            ganancia = total_v - total_d
            produc = total_i - total_v
            datos.append({'tipo': tipo, 'total_ingresos': total_i, 'total_devoluciones': total_d, 'total_ventas': total_v, 'resta': resta, 'ganancia': ganancia, 'total_pagado': total_p, 'produccion': produc})
            totales['ingresos'] += total_i
            totales['ventas'] += total_v
            totales['devoluciones'] += total_d
            totales['resta'] += resta
            totales['pagado'] += total_p
            totales['produccion'] += produc
            totales['ganancia'] += ganancia
        egresos = Egreso.objects.filter(fecha__lte=fecha_fin, fecha__gte=fecha_ini)
        total_egre = egresos.aggregate(total=Sum('monto'))
        if len(egresos) >= 1:
            total_e = total_egre['total']
        else:
            total_e = 0
        totales['ganancia_neta'] = totales['ganancia'] - total_e
    return render_to_response('reporte_ganancias.html', {'datos': datos, 'formulario': formulario, 'fecha_ini': fecha_ini, 'fecha_fin': fecha_fin, 'total_egresos': total_e, 'totales': totales}, context_instance=RequestContext(request))


@login_required
def venta(request):
    if request.method == 'POST':
        formulario = VentaForm(request.POST)
        if formulario.is_valid():
            venta = formulario.save()
            tipo_pan = venta.tipopan
            produccion = Producion.objects.get(pk=tipo_pan)
            produccion.stock = produccion.stock - venta.cantidad
            produccion.save()
            deudores = Deuda.objects.filter(tipopan=tipo_pan, cliente=venta.cliente)
            if len(deudores) > 0:
                deudor = deudores[0]
                deudor.monto = deudor.monto + (venta.cantidad * tipo_pan.precio)
                if deudor.monto > 0:
                    deudor.cancelado = False
                deudor.save()
            else:
                deudor = Deuda(tipopan=tipo_pan, cliente=venta.cliente, monto=(venta.cantidad * tipo_pan.precio), cancelado=False)
                deudor.save()
            instancia = Venta(cliente=venta.cliente)
            formulario = VentaForm(instance=instancia)
    else:
        formulario = VentaForm()
    return render_to_response('venta.html', {'formulario': formulario}, context_instance=RequestContext(request))


@login_required
def venta_grupal(request, id_cliente):
    contador_guardados = 0
    guardados = []
    clientes = Cliente.objects.all()
    tipos_total = len(TipoPan.objects.all())
    VentaFormSet = formset_factory(VentaForm_s, formset=BaseVentaFormSet, max_num=tipos_total)
    inicial = inicial_venta(id_cliente)
    if request.method == 'POST':
        enviar = VentaFormSet(request.POST)
        for x in enviar:
            if x.is_valid():
                input_cantidad = x.__getitem__('cantidad')
                try:
                    input_cantidad = str(input_cantidad).split('value="')[1].split('"')[0]
                    if int(input_cantidad) > 0:
                        guardado = x.save()
                        try:
                            produ = Producion.objects.get(pk=guardado.tipopan)
                            produ_mod = produ
                            produ_mod.stock = produ_mod.stock - guardado.cantidad
                            produ_mod.save()
                        except:
                            produ_mod = Producion(tipopan=guardado.tipopan, stock=guardado.cantidad)
                            produ_mod.save()
                        deudores = Deuda.objects.filter(tipopan=guardado.tipopan, cliente=guardado.cliente)
                        if len(deudores) > 0:
                            deudor = deudores[0]
                            deudor.monto = deudor.monto + (guardado.cantidad * guardado.tipopan.precio)
                            if deudor.monto > 0:
                                deudor.cancelado = False
                            deudor.save()
                        else:
                            deudor = Deuda(tipopan=guardado.tipopan, cliente=guardado.cliente, monto=(guardado.cantidad * guardado.tipopan.precio), cancelado=False)
                            deudor.save()
                        guardados.append({'tipo': guardado.tipopan, 'cantidad': guardado.cantidad})
                        contador_guardados += 1
                except:
                    pass
            else:
                pass
    else:
        enviar = VentaFormSet(initial=inicial)
    if contador_guardados > 0:
        inicial = inicial_venta(id_cliente)
        enviar = VentaFormSet(initial=inicial)
    return render_to_response('venta_grupal.html', {'formset': enviar, 'guardados': contador_guardados, 'guardados_list': guardados, 'clientes': clientes, 'id_cliente': id_cliente}, context_instance=RequestContext(request))


@login_required
def deudores(request):
    cliente_form = ClienteSeleccionForm
    if request.method == 'POST':
        cliente_sele = request.POST['cliente']
        if cliente_sele == '':
            return HttpResponseRedirect('/ventas/deudores/')
        return HttpResponseRedirect('/ventas/deudores/' + cliente_sele + "/")
    deudores = Deuda.objects.filter(cancelado=False)
    return render_to_response('deudores.html', {'deudores': deudores, 'cliente_form': cliente_form}, context_instance=RequestContext(request))


@login_required
def deudores_cliente(request, codigo):
    cliente_form = ClienteSeleccionForm
    if request.method == 'POST':
        cliente_sele = request.POST['cliente']
        if cliente_sele == '':
            return HttpResponseRedirect('/ventas/deudores/')
        return HttpResponseRedirect('/ventas/deudores/' + cliente_sele + "/")
    try:
        cliente_sele = Cliente.objects.get(pk=int(codigo))
        deudores = Deuda.objects.filter(cancelado=False, cliente=cliente_sele)
    except:
        deudores = Deuda.objects.filter(cancelado=False)
    return render_to_response('deudores.html', {'deudores': deudores, 'cliente_form': cliente_form}, context_instance=RequestContext(request))


@login_required
def pagar(request, codigo):
    deuda = Deuda.objects.get(pk=codigo)
    cant_restante = deuda.monto
    if request.method == 'POST':
        instancia = Pago(deuda=deuda)
        formulario = PagoForm(request.POST, instance=instancia)
        if formulario.is_valid():
            pago = formulario.save()
            deuda.monto = pago.restante
            if deuda.monto <= 0:
                deuda.cancelado = True
            deuda.save()
            return HttpResponseRedirect('/ventas/deudores/')
    else:
        instancia = Pago(total=deuda.monto, monto=0, restante=deuda.monto)
        formulario = PagoForm(instance=instancia)
    return render_to_response('pagar.html', {'formulario': formulario, 'cant_restante': cant_restante}, context_instance=RequestContext(request))


@login_required
def devolucion(request):
    mensaje = ''
    if request.method == 'POST':
        formulario = DevolucionForm(request.POST)
        if formulario.is_valid():
            devolucion = formulario.save()
            tipo_pan = devolucion.tipopan
            #produccion = Producion.objects.get(pk=tipo_pan)
            #produccion.stock = produccion.stock - devolucion.cantidad
            #produccion.save()
            deudores = Deuda.objects.filter(tipopan=tipo_pan, cliente=devolucion.cliente)
            if len(deudores) > 0:
                deudor = deudores[0]
                deudor.monto = deudor.monto - (devolucion.cantidad * tipo_pan.precio)
                if deudor.monto > 0:
                    deudor.cancelado = False
                elif deudor.monto <= 0:
                    deudor.cancelado = True
                deudor.save()
            instancia = Devolucion(cliente=devolucion.cliente)
            formulario = DevolucionForm(instance=instancia)
            mensaje = 'Devolucion echa satisfactoriamente.'
    else:
        formulario = DevolucionForm()
    return render_to_response('devolucion.html', {'formulario': formulario, 'mensaje': mensaje}, context_instance=RequestContext(request))


@login_required
def devolucion_grupal(request, id_cliente):
    contador_guardados = 0
    guardados = []
    clientes = Cliente.objects.all()
    tipos_total = len(TipoPan.objects.all())
    DevolucionFormSet = formset_factory(DevolucionForm_g, formset=BaseDevolucionFormSet, max_num=tipos_total)
    inicial = inicial_devolucion(id_cliente)
    if request.method == 'POST':
        enviar = DevolucionFormSet(request.POST)
        for x in enviar:
            if x.is_valid():
                input_cantidad = x.__getitem__('cantidad')
                try:
                    input_cantidad = str(input_cantidad).split('value="')[1].split('"')[0]
                    if int(input_cantidad) > 0:
                        guardado = x.save()
                        try:
                            produ = Producion.objects.get(pk=guardado.tipopan)
                            produ_mod = produ
                            produ_mod.stock = produ_mod.stock + guardado.cantidad
                            produ_mod.save()
                        except:
                            produ_mod = Producion(tipopan=guardado.tipopan, stock=guardado.cantidad)
                            produ_mod.save()
                        deudores = Deuda.objects.filter(tipopan=guardado.tipopan, cliente=guardado.cliente)
                        if len(deudores) > 0:
                            deudor = deudores[0]
                            deudor.monto = deudor.monto - (guardado.cantidad * guardado.tipopan.precio)
                            if deudor.monto > 0:
                                deudor.cancelado = False
                            elif deudor.monto <= 0:
                                deudor.cancelado = True
                            deudor.save()
                        else:
                            deudor = Deuda(tipopan=guardado.tipopan, cliente=guardado.cliente, monto=(guardado.cantidad * guardado.tipopan.precio), cancelado=False)
                            deudor.save()
                        guardados.append({'tipo': guardado.tipopan, 'cantidad': guardado.cantidad})
                        contador_guardados += 1
                except:
                    pass
            else:
                pass
    else:
        enviar = DevolucionFormSet(initial=inicial)
    if contador_guardados > 0:
        inicial = inicial_devolucion(id_cliente)
        enviar = DevolucionFormSet(initial=inicial)
    return render_to_response('devolucion_grupal.html', {'formset': enviar, 'guardados': contador_guardados, 'guardados_list': guardados, 'clientes': clientes, 'id_cliente': id_cliente}, context_instance=RequestContext(request))


@login_required
def modificar_venta(request, codigo):
    venta = Venta.objects.get(pk=codigo)
    if request.method == 'POST':
        cant_ant = venta.cantidad
        precio_ant = venta.precio()
        formu = VentaForm(request.POST, instance=venta)
        if formu.is_valid():
            guardado = formu.save()
            if cant_ant != guardado.cantidad:
                #eliminar el anterior
                deuda = Deuda.objects.filter(cliente=guardado.cliente, tipopan=guardado.tipopan)[0]
                deuda.monto = deuda.monto - precio_ant
                deuda.save()
                produ = Producion.objects.get(pk=guardado.tipopan)
                produ.stock = produ.stock + cant_ant
                produ.save()
                #agregar el nuevo
                deuda.monto = deuda.monto + guardado.precio()
                produ.stock = produ.stock - guardado.cantidad
                if deuda.monto <= 0:
                    deuda.cancelado = True
                deuda.save()
                produ.save()
            return HttpResponseRedirect('/reporte/ventas/')
    else:
        formu = VentaForm(instance=venta)
    return render_to_response('venta_editar.html', {'formu': formu}, context_instance=RequestContext(request))


def datos_pan(request, codigo):
    """Devuelve datos de un tipo de pan para la produccion"""
    tipo_pan = TipoPan.objects.get(pk=int(codigo))
    produccion = Producion.objects.filter(tipopan=tipo_pan)[0]
    new_result = []
    datos = {}
    datos['stock'] = produccion.stock
    datos['precio'] = str(tipo_pan.precio)
    new_result.append(datos)
    return HttpResponse(json.dumps(new_result))


def datos_deuda(request, id_pan, id_cliente):
    """Devuelve datos de la deuda de un tipo de pan y cliente"""
    tipo_pan = TipoPan.objects.get(pk=int(id_pan))
    cliente = Cliente.objects.get(pk=int(id_cliente))
    deuda = Deuda.objects.filter(tipopan=tipo_pan, cliente=cliente)[0]
    new_result = []
    datos = {}
    if deuda:
        datos['monto'] = str(deuda.monto)
        datos['cantidad'] = str(int(round(deuda.monto / tipo_pan.precio, 0)))
    new_result.append(datos)
    return HttpResponse(json.dumps(new_result))


def eliminar_venta(request, codigo):
    """Elimina un venta echa"""
    venta = Venta.objects.get(pk=int(codigo))
    deuda = Deuda.objects.filter(cliente=venta.cliente, tipopan=venta.tipopan)[0]
    deuda.monto = deuda.monto - venta.precio()
    if deuda.monto <= 0:
        deuda.cancelado = True
    deuda.save()
    produ = Producion.objects.get(pk=venta.tipopan)
    produ.stock = produ.stock + venta.cantidad
    produ.save()
    venta.delete()
    new_result = []
    datos = {}
    datos['resultado'] = "True"
    new_result.append(datos)
    return HttpResponse(json.dumps(new_result))


def eliminar_egreso(request, codigo):
    """Elimina un venta echa"""
    venta = Egreso.objects.get(pk=int(codigo))
    venta.delete()
    new_result = []
    datos = {}
    datos['resultado'] = "True"
    new_result.append(datos)
    return HttpResponse(json.dumps(new_result))


def conteos():
    tipos_pan = TipoPan.objects.all()
    inicial = []
    for tipo in tipos_pan:
        stock_ini = 0
        produ = Producion.objects.filter(tipopan=tipo)
        if len(produ) > 0:
            stock_ini = produ[0].stock
        inicial.append({'tipopan': tipo, 'precio': tipo.precio, 'saldo_inicial': stock_ini})
    return inicial


def inicial_venta(id_cliente):
    tipos_pan = TipoPan.objects.all()
    inicial = []
    cliente = Cliente.objects.get(pk=int(id_cliente))
    for tipo in tipos_pan:
        stock_ini = 0
        produ = Producion.objects.get(pk=tipo)
        stock_ini = produ.stock
        inicial.append({'tipopan': tipo, 'cliente': cliente, 'total': stock_ini, 'restantes': stock_ini, 'precio': tipo.precio})
    return inicial


def inicial_devolucion(id_cliente):
    tipos_pan = TipoPan.objects.all()
    inicial = []
    cliente = Cliente.objects.get(pk=int(id_cliente))
    for tipo in tipos_pan:
        stock_ini = 0
        deuda = Deuda.objects.filter(tipopan=tipo, cliente=cliente)
        if deuda:
            deuda = deuda[0]
            stock_ini = str(int(round(deuda.monto / tipo.precio, 0)))
        inicial.append({'tipopan': tipo, 'cliente': cliente, 'total': stock_ini})
    return inicial
