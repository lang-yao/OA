#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@author: 4rat
@time: 2020/2/18 15:08
"""
from django import template

register = template.Library()


@register.filter(name='join_members')
def join(value, arg):
    return arg.join(x.name + '-' + x.staff_id for x in value)
