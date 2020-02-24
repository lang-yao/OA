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
    path('admin_user_add/', views.admin_user_add, name='管理人员添加'),

    path('tjd_list/', views.tjd_list, name='管理员突击队模块'),
    path('tjd_add/', views.tjd_add, name='突击队人员添加'),
    path('tjd_update/<tjd_id>/', views.tjd_update, name='突击队人员修改'),

    path('del/', views.staff_del, name='人员删除'),

    path('manager_user_list/', views.manager_user_list, name='管理员项目经理模块'),
    path('manager_user_add/', views.manager_user_add, name='项目经理人员添加'),

    path('admin_xqadd/', views.admin_xqadd, name='新增需求模块'),
    path('admin_xqaddcl/', views.admin_xqaddcl, name='新增需求处理模块'),
    path('admin_xqaddhistory/', views.admin_xqaddhistory, name='历史需求模块'),
    path('admin_xqcl/', views.admin_xqcl, name='需求变更模块'),

    # path('admingroup/',views.admin_group,name ='添加管理组'),
    # path('xmgroup/',views.xm_group,name ='添加项目组'),
    # path('xm_user_add/',views.xm_group,name ='添加项目人员'),
]
