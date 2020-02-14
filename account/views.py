from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, Group, ContentType
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate
from django.contrib import auth
# Create your views here.
from manageradmin.models import Tjd_staff
from .models import User


def user_login(request):
    '''用户登陆'''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        '''判断登陆用户是否填写完整登录信息'''
        if not all([username, password]):
            error = '请填写完整的登录信息'
            return render(request, 'login.html', {'error': error})
        user = auth.authenticate(request, username=username, password=password)
        '''判断用户是否合法'''
        if user is not None:
            auth.login(request, user)
            request.session['user_id'] = user.id
            usergroup = Group.objects.get(user=user)
            request.session['user_group'] = str(usergroup)
            # 清除过期的session
            request.session.clear_expired()
            print('用户所属组：', usergroup)
            userpermissions = user.get_group_permissions()
            print('用户权限：', userpermissions)
            if user.has_perms(['account.add_user']):
                # if user.is_superuser:   #判断用户是否是管理员
                print('返回管理员默认页面')
                return redirect('管理员默认页面模块')
            else:
                print('返回项目经理默认页面')
                return redirect('项目经理默认页面模块')
        else:
            # 验证失败，账号或密码错误
            error = '账户或密码错误，请重新登陆'
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')
        #return redirect('login')


@login_required(login_url='login')
# def user_logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         return redirect('login')
def user_logout(request):
    '''用户登出'''
    request.session.flush()
    auth.logout(request)
    return redirect('login')


from django.conf import settings
from django.core.mail import EmailMultiAlternatives
