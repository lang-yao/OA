#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@author: 4rat
@time: 2020/1/19 13:51
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),

]
