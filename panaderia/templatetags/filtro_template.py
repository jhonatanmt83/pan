# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter(name='reemplaza')
def reemplaza(objecto):
    devolver = 0
    for x in objecto:
        devolver = devolver + x.precio()
    return devolver
