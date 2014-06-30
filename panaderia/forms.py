# -*- coding: utf-8 -*-
from django import forms
#from django.forms import ModelForm
from panaderia.models import TipoAlmacen, TipoPan, Producion, Cliente, Ingreso, Venta, Deuda, Pago, Egreso, Devolucion
from django.forms import TextInput, Select
from django.forms.formsets import formset_factory, BaseFormSet
from bootstrap_toolkit.widgets import BootstrapDateInput
import datetime


class formingreso(forms.Form):
    usuarioform = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Usuario'}
            )
        )
    passform = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            render_value=False,
            attrs={'placeholder': 'Contraseña'}
            )
        )
    #comment = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email address'}))


class formpassword(forms.Form):
    passform1 = forms.CharField(
        label='Nueva Contraseña',
        widget=forms.PasswordInput(
            render_value=False,
            )
        )
    passform2 = forms.CharField(
        label='Vuelva a escribir su contraseña',
        widget=forms.PasswordInput(
            render_value=False,
            )
        )


class TipoAlmacenForm(forms.ModelForm):
    class Meta:
        model = TipoAlmacen


class TipoPanForm(forms.ModelForm):
    class Meta:
        model = TipoPan


class ProducionForm(forms.ModelForm):
    class Meta:
        model = Producion


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente


class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        widgets = {
            'cantidad': TextInput(attrs={'onkeyup': 'precio_total(this)',
                'onkeypress': 'return AcceptNum(event)'}),
            'tipopan': Select(attrs={'disabled': 'disabled'})
        }


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        widgets = {
            'cantidad': TextInput(attrs={'onkeyup': 'verificar_datos();',
                'onkeypress': 'return AcceptNum(event)'}),
            'tipopan': Select(attrs={'onchange': 'obtener_datos();'}),
         }


class VentaForm_s(forms.ModelForm):
    class Meta:
        model = Venta
        widgets = {
            'cantidad': TextInput(attrs={'onkeyup': 'verificar_datos(this);',
                'onkeypress': 'return AcceptNum(event)'}),
            'tipopan': Select(attrs={'disabled': 'disabled'})
         }


class DeudaForm(forms.ModelForm):
    class Meta:
        model = Deuda


class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        exclude = ('deuda')
        fields = ('monto', 'total', 'restante')
        widgets = {
            'monto': TextInput(attrs={'onkeyup': 'actualiza_campos();'}),
            'total': TextInput(attrs={'readonly': 'readonly'}),
            'restante': TextInput(attrs={'readonly': 'readonly'}),
         }


class EgresoForm(forms.ModelForm):
    class Meta:
        model = Egreso
        widgets = {
            'monto': TextInput(attrs={
                'onkeypress': 'return AcceptNum(event)'
                })
         }


class BaseIngresoFormSet(BaseFormSet):
    def add_fields(self, form, index):
        super(BaseIngresoFormSet, self).add_fields(form, index)
        form.fields["saldo_inicial"] = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        form.fields["precio"] = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        form.fields["precio_total"] = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))


class BaseVentaFormSet(BaseFormSet):
    def add_fields(self, form, index):
        super(BaseVentaFormSet, self).add_fields(form, index)
        form.fields["total"] = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        form.fields["restantes"] = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        form.fields["precio"] = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        form.fields["valor"] = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))


class TipoPanSelect(forms.ModelForm):
    class Meta:
        model = Ingreso
        exclude = ('cantidad', 'fecha')


class FechasForm(forms.Form):
    fecha1 = forms.DateField(
        widget=BootstrapDateInput(),
        label='Desde'
    )
    fecha2 = forms.DateField(
        widget=BootstrapDateInput(),
        label='Hasta'
    )


class FechaForm(forms.Form):
    fecha = forms.DateField(
        widget=BootstrapDateInput(),
        label='Fecha',
        initial=datetime.date.today
    )


class ClienteSeleccionForm(forms.ModelForm):
    class Meta:
        model = Deuda
        exclude = ('tipopan', 'monto', 'cancelado')


class DevolucionForm(forms.ModelForm):
    class Meta:
        model = Devolucion
        widgets = {
            'cantidad': TextInput(attrs={'onkeyup': 'verificar_datos();',
                'onkeypress': 'return AcceptNum(event)'}),
            'tipopan': Select(attrs={'onchange': 'obtener_datos();'}),
            'cliente': Select(attrs={'onchange': 'obtener_datos();'}),
        }


class DevolucionForm_g(forms.ModelForm):
    class Meta:
        model = Devolucion
        widgets = {
            'cantidad': TextInput(attrs={'onkeyup': 'verificar_datos(this);',
                'onkeypress': 'return AcceptNum(event)'}),
            'tipopan': Select(attrs={'disabled': 'disabled'})
        }


class BaseDevolucionFormSet(BaseFormSet):
    def add_fields(self, form, index):
        super(BaseDevolucionFormSet, self).add_fields(form, index)
        form.fields["total"] = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
