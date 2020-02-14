#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .models import User

"""
@author: 4rat
@time: 2020/2/12 09:08
"""


#  上下文处理器全局获取用户组
def front_user(request):
    user_id = request.session.get('user_id')
    user_group = request.session.get('user_group')
    # print(user_id,' |||  ',user_group)
    context = {}
    context['user_id'] = user_id
    context['user_group'] = user_group
    # print(context)
    return context

    # print(context)

    # if user_id:
    #     try:
    #         user = User.objects.get(pk = user_id)
    #         context['front_user'] = user
    #         context['front_group'] = user_group
    #         #print(context)
    #     except:
    #         pass
    # return context
