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
    path('manager_xqhistory/', views.manager_xqhistory, name='项目经理需求历史模块'),

    path('query_demand_person/', views.query_demand_staff, name='人员查询模块'),
    path('deman_access/', views.deman_access, name='人员评价模块'),
]
