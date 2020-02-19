#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@author: 4rat
@time: 2020/1/20 14:09
"""
from django.urls import path
from . import views


urlpatterns = [
    path('manager_index/', views.manager_index, name='项目经理默认页面模块'),
    path('manager_xqadd/', views.manager_xqadd, name='项目经理需求增加模块'),
    path('manager_xqhistory', views.manager_xqhistory, name='项目经理需求历史模块'),
]
