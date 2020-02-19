# -*- coding: utf-8 -*-
# @Time    : 20/02/18 14:39
# @Author  : sloth
# @File    : myjoin.py.py

from django import template

register = template.Library()


@register.filter(name='join')
def join(value, arg):
    return arg.join(x.name + '-' + x.staff_id for x in value)
