from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth import authenticate
from django.contrib import auth
from django.shortcuts import redirect


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        # 判断用户是否合法
        if user is not None:
            print(user)
            # 进行权限判断，跳转不同页面
            # return render(request, 'admin_index.html')
            # return render(request,'manageradmin/admin_index')
            auth.login(request, user)
            return redirect('管理员默认页面模块')

        else:
            # 验证失败，暂时不做处理
            # return redirect('login',{'error':'账户或密码错误，请重新登陆'})
            return render(request, 'login.html', {'error': '账户或密码错误，请重新登陆'})
    else:
        return render(request, 'login.html')
        # return redirect('login')


def user_logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # return render(request, 'login.html')
        return redirect('login')
