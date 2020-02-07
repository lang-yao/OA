#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@author: 4rat
@time: 2020/1/20 14:09
"""
from django.urls import path
from . import views

urlpatterns = [
    path('admin_index/', views.tjd_index, name='管理员默认页面模块'),
    path('tjd_list/', views.tjd_list, name='管理员突击队模块'),
    path('tjd_add/', views.tjd_add, name='突击队人员添加'),
    path('tjd_del/', views.tjd_del, name='突击队人员删除'),
    # path('tjd_del/<tjd_list.id>', views.tjd_del, name='突击队人员删除'),
    path('xmjl/', views.xmjl)
]
