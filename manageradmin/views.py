from django.shortcuts import render
from django.http import HttpResponse
from .models import Tjd_staff
from django.shortcuts import redirect
from django.contrib.auth.decorators import permission_required
from account.models import User
from django.contrib.auth.models import Group, ContentType, Permission
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
# 访问限制模块 @login_required
from django.contrib.auth.decorators import login_required


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def tjd_index(request):
    '''突击队人员总数'''
    # 突击队人员总数
    tjds = Tjd_staff.objects.all().count()
    # 已分配的突击队人员总数
    tjds0 = Tjd_staff.objects.filter(zhuangtai=0).count()
    # 未分配的突击队人员总数
    tjds1 = Tjd_staff.objects.filter(zhuangtai=1).count()
    # 获取项目组人数总数
    xmjlrs = User.objects.filter(groups__name='项目组').count()
    # 获取总项目需求
    xmsqds = Xmsqd.objects.filter(zhuangtai='1').count()
    # 获取新增需求
    xmsqds1 = Xmsqd.objects.filter(zhuangtai='0').count()
    return render(request, 'admin_index.html',
                  {'data': tjds, 'data0': tjds0, 'data1': tjds1, 'data2': xmjlrs, 'data3': xmsqds, 'data4': xmsqds1})


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def tjd_list(request):
    '''突击队列表'''
    tjds = Tjd_staff.objects.all()
    context = {}
    context['tjds'] = tjds
    return render(request, 'admin_staff_tjd.html', context)


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def tjd_add(request):
    '''突击队人员添加'''
    if request.method == 'POST':
        name = request.POST['name']
        staff_id = request.POST['staff_id']
        jineng = request.POST.getlist('jineng')
        ruzhitime = request.POST['ruzhitime']
        fazhan = request.POST['fazhan']
        diqu = request.POST['diqu']
        dengji = request.POST['dengji']
        zhuangtai = request.POST['zhuangtai']
        # 获取post到models模型中
        tjd_staff = Tjd_staff()
        tjd_staff.name = name
        tjd_staff.staff_id = staff_id
        tjd_staff.jineng = jineng
        tjd_staff.ruzhitime = ruzhitime
        tjd_staff.fazhan = fazhan
        tjd_staff.diqu = diqu
        tjd_staff.dengji = dengji
        tjd_staff.zhuangtai = zhuangtai
        # 写入
        tjd_staff.save()
        return redirect('管理员突击队模块')
    else:
        return redirect('管理员突击队模块')


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def tjd_del(request):
    '''突击队人员删除'''
    id = request.POST['id']
    tjd_renyuan = Tjd_staff.objects.get(id=id)
    tjd_renyuan.delete()
    return redirect('管理员突击队模块')


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def tjd_update(request, tjd_id):
    '''突击队人员编辑'''
    tjd_renyuan = Tjd_staff.objects.get(id=tjd_id)
    return HttpResponse(tjd_id)
    # return redirect('管理员突击队模块')


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def xmjl_list(request):
    '''项目经理列表'''
    # xmjls = User.objects.all()
    xmjls = User.objects.filter(groups__name='项目组')
    for i in xmjls:
        print('项目组用户:', i.username)
        print('用户名称:', i.first_name)
    context = {}
    context['xmjls'] = xmjls
    return render(request, 'admin_staff_xmjl.html', context)


# def xm_group(request):
#     '''创建项目组权限'''
#     if Group.objects.filter(name='项目组').first():                            #判断是否存在项目组如果不存在则创建
#         group = Group.objects.create(name='项目组')                              #创建项目组
#         content_type = ContentType.objects.get_for_model(Xmsqd)              #通过model或者model的实例来寻找ContentType类型
#         permissions = Permission.objects.filter(content_type=content_type)      #获取model实例的全部权限列表
#         permissions = (permissions[0],permissions[3])                           #配置增加和查看权限
#         group.permissions.set(permissions)                                      #添加分组权限
#
#
#         return HttpResponse('创建项目组分组权限成功')
#
#     else:
#
#         return HttpResponse('创建分组权限成功')
# group = Group.objects.create(name='项目组')                              #创建项目组
# content_type = ContentType.objects.get_for_model(Xmsqd)              #通过model或者model的实例来寻找ContentType类型
# permissions = Permission.objects.filter(content_type=content_type)      #获取model实例的全部权限列表
# permissions = (permissions[0],permissions[3])                           #配置增加和查看权限
# group.permissions.set(permissions)                                      #添加分组权限
# return HttpResponse('创建项目组分组权限成功')

# group.permissions.add(permissions[3])                                               #添加权限。
#     # group.permissions.remove：                                               #移除权限。
#     # group.permissions.clear：                                                #清除所有权限。
#     group.save()
#     # return HttpResponse('创建分组权限成功')
#
#     group = Group.objects.filter(name = '项目组').first()                              #获取项目组
#     user = User.objects.first()
#     user.groups.add(group)
#     user.save()
#     yonghuquanxian =  user.get_group_permissions()                                                     #获取用户所属组的权限
#     print('yonghuquanxian',yonghuquanxian)
#     # user.save()
#     # return HttpResponse('添加用户进入分组权限成功')
#     # user = User.objects.first()
#
#     # if user.has_perms(['login.view_wenzhang,login.edit_wenzhang']):                  #判断用户有没有多个权限
#     # if user.has_perm('login.view_wenzhang'):  # 判断用户有没有权限
#     #     print('有权限')
#     # else:
#     #     print('没有权限')
#     return HttpResponse('创建项目组成功')

# def admin_group(request):
#     '''创建管理组权限'''
#     group = Group.objects.create(name='管理组')                              #创建项目组
#     '''获取USER模型全部权限'''
#     content_type = ContentType.objects.get_for_model(User)              #通过model或者model的实例来寻找ContentType类型
#     permissions = Permission.objects.filter(content_type=content_type)      #获取model实例的全部权限列表
#     group.permissions.set(permissions)                                      #添加分组权限
#     print('user权限', permissions)
#     group.save()
#     '''获取Tjd_staff模型全部权限'''
#     content_type = ContentType.objects.get_for_model(Tjd_staff)              #通过model或者model的实例来寻找ContentType类型
#     permissions = Permission.objects.filter(content_type=content_type)      #获取model实例的全部权限列表
#     group.permissions.add(*permissions)                                      #添加分组权限
#     print('突击队权限', permissions)
#     group.save()
#
#     '''获取Xmsqd模型查看修改权限'''
#     content_type = ContentType.objects.get_for_model(Xmsqd)              #通过model或者model的实例来寻找ContentType类型
#     permissions = Permission.objects.filter(content_type=content_type)      #获取model实例的全部权限列表
#     permissions = (permissions[1],permissions[3])                           #配置增加和查看权限
#     group.permissions.add(*permissions)                                      #添加分组权限
#     return HttpResponse('创建管理组分组权限成功')


def admin_user_add(request):
    '''添加管理组及人员，后期需要更改防止bug'''
    # if request.method == 'POST':
    if Group.objects.filter(name='管理组').first():  # 判断是否存在项目组如果不存在则创建
        print('管理组存在')

        username = 'admina'
        password = '123'
        iphone = '1202111111'
        email = '12@qq.com'
        diqu = '陕西'
        staff_id = 'A1'
        first_name = '管理员'

        # username = request.POST['username']
        # first_name = request.POST['first_name']
        # staff_id = request.POST['staff_id']
        # iphone = request.POST['iphone']
        # email = request.POST['email']
        # password = request.POST['password']
        # diqu = request.POST['diqu']
        user = User.objects.create_user(username=username, first_name=first_name, staff_id=staff_id, iphone=iphone,
                                        email=email, password=password, diqu=diqu)
        group = Group.objects.filter(name='管理组').first()  # 获取项目组
        user.groups.add(group)
        user.save()
        msg = '添加成功'
        print(msg)
        return HttpResponse('管理组存在，用户已添加')
        # return render(request, 'admin_staff_xmjl.html', {'msg': msg})
    else:
        group = Group.objects.create(name='管理组')  # 创建项目组
        '''获取USER模型全部权限'''
        content_type = ContentType.objects.get_for_model(User)  # 通过model或者model的实例来寻找ContentType类型
        permissions = Permission.objects.filter(content_type=content_type)  # 获取model实例的全部权限列表
        group.permissions.set(permissions)  # 添加分组权限
        # print('user权限', permissions)
        group.save()
        '''获取Tjd_staff模型全部权限'''
        content_type = ContentType.objects.get_for_model(Tjd_staff)  # 通过model或者model的实例来寻找ContentType类型
        permissions = Permission.objects.filter(content_type=content_type)  # 获取model实例的全部权限列表
        group.permissions.add(*permissions)  # 添加分组权限
        # print('管理组权限', permissions)
        group.save()
        '''获取Xmsqd模型查看修改权限'''
        content_type = ContentType.objects.get_for_model(Xmsqd)  # 通过model或者model的实例来寻找ContentType类型
        permissions = Permission.objects.filter(content_type=content_type)  # 获取model实例的全部权限列表
        permissions = (permissions[1], permissions[3])  # 配置增加和查看权限
        group.permissions.add(*permissions)  # 添加分组权限
        group.save()

        iphone = '1202111110'
        username = 'admin'
        password = '123'
        email = '1@qq.com'
        diqu = '陕西'
        staff_id = 'A0'
        first_name = '管理员'

        # username = request.POST['username']
        # first_name = request.POST['first_name']
        # staff_id = request.POST['staff_id']
        # iphone = request.POST['iphone']
        # email = request.POST['email']
        # password = request.POST['password']
        # diqu = request.POST['diqu']
        user = User.objects.create_user(username=username, first_name=first_name, staff_id=staff_id, iphone=iphone,
                                        email=email, password=password, diqu=diqu)
        group = Group.objects.filter(name='管理组').first()  # 获取管理组
        user.groups.add(group)
        user.save()
        msg = '管理组不存在，创建管理组成功，添加成功'
        print(msg)
        return HttpResponse('管理组不存在，创建管理组成功，添加成功')
        # return render(request, 'admin_staff_xmjl.html', {'msg': msg})
    # else:
    #     return redirect('管理员项目经理模块')


from manager.models import Xmsqd


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def manager_user_add(request):
    '''项目经理人员添加'''
    if request.method == 'POST':
        if Group.objects.filter(name='项目组').first():  # 判断是否存在项目组如果不存在则创建
            print('项目组存在')
            username = request.POST['username']
            first_name = request.POST['first_name']
            staff_id = request.POST['staff_id']
            iphone = request.POST['iphone']
            email = request.POST['email']
            password = request.POST['password']
            diqu = request.POST['diqu']
            user = User.objects.create_user(username=username, first_name=first_name, staff_id=staff_id, iphone=iphone,
                                            email=email, password=password, diqu=diqu)
            group = Group.objects.filter(name='项目组').first()  # 获取项目组
            user.groups.add(group)
            user.save()
            msg = '添加成功'
            print(msg)
            return redirect('管理员项目经理模块')
        else:
            print('项目组不存在')
            group = Group.objects.create(name='项目组')  # 创建项目组
            content_type = ContentType.objects.get_for_model(Xmsqd)  # 通过model或者model的实例来寻找ContentType类型
            permissions = Permission.objects.filter(content_type=content_type)  # 获取model实例的全部权限列表
            permissions = (permissions[0], permissions[3])  # 配置增加和查看权限
            group.permissions.set(permissions)  # 添加分组权限
            group.save()

            username = request.POST['username']
            first_name = request.POST['first_name']
            staff_id = request.POST['staff_id']
            iphone = request.POST['iphone']
            email = request.POST['email']
            password = request.POST['password']
            diqu = request.POST['diqu']
            user = User.objects.create_user(username=username, first_name=first_name, staff_id=staff_id, iphone=iphone,
                                            email=email, password=password, diqu=diqu)
            group = Group.objects.filter(name='项目组').first()  # 获取项目组
            user.groups.add(group)
            user.save()
            msg = '创建项目组成功，添加成功'
            print(msg)
            return redirect('管理员项目经理模块')
    else:
        return redirect('管理员项目经理模块')

    # '''项目经理人员添加'''
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     first_name = request.POST['first_name']
    #     staff_id = request.POST['staff_id']
    #     iphone = request.POST['iphone']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     diqu = request.POST['diqu']
    #     user = User.objects.create_user(username=username,first_name=first_name,staff_id=staff_id,iphone=iphone,email=email,password=password, diqu=diqu)
    #     #return HttpResponse('添加项目经理成功')
    #     #msg = '添加成功'
    #     #print(msg)
    #     #return render(request, 'admin_staff_xmjl.html', {'msg': msg})
    #     return redirect('管理员项目经理模块')
    # else:
    #     msg = '添加失败'
    #     print(msg)
    #     return render(request, 'admin_staff_xmjl.html', {'msg': msg})
    # '''管理权限'''
    # iphone = '12021111111'
    # username = 'admin'
    # password = '66666666666'
    # email = '112211211@qq.com'
    # diqu = '陕西'
    # staff_id = 'A1'
    # user = User.objects.create_user(iphone=iphone,username=username,password=password,staff_id= staff_id,email=email,
    #                                  diqu=diqu)
    # print('创建用户：',user.username,user.diqu,user.staff_id)
    # group = Group.objects.filter(name='项目组').first()
    # user.groups.add(group)
    # user.save()
    # print('加入管理组')
    # yonghuquanxian =  user.get_group_permissions()                                                     #获取用户所属组的权限
    # for i in yonghuquanxian:
    #     print(i)
    # return HttpResponse('创建用户啦')


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def manager_user_del(request):
    '''项目经理人员删除'''
    pass


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def manager_user_update(request):
    '''项目经理人员更新'''
    pass


from manager.models import Xmsqd


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def admin_xqadd(request):
    '''管理员项目总需求列表，获取待处理的订单'''
    Xmsqds = Xmsqd.objects.filter(zhuangtai='0')
    # Xmsqds = Xmsqd.objects.all()
    context = {}
    context['Xmsqds'] = Xmsqds
    return render(request, 'admin_staff_demands_add.html', context)


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def admin_xqaddhistory(request):
    Xmsqds = Xmsqd.objects.all()
    context = {}
    context['Xmsqds'] = Xmsqds
    return render(request, 'admin_staff_demands_history.html', context)


from django.conf import settings

email = 'liuhao07@qianxin.com'
code = '123'


def xmcl_email(request):
    '''处理订单后邮件功能模块'''
    fpry = Tjd_staff.objects.filter(id=11).first()
    fpry = {
        'staff_id': fpry.staff_id,
        'name': fpry.name,
    }
    print(fpry['name'], '(', fpry['staff_id'], ')')

    # Xmsqds = Xmsqd.objects.filter(id=8)
    # for i in Xmsqds:
    #     print(i.xmname)
    #     print(i.cjtime)
    #     print(i.fpry)
    #     print(i.kstime)
    #     print(i.jstime)
    # print(Xmsqds)
    # context = {}
    # context['Xmsqds'] = Xmsqds
    # for i in context:
    #     print(i)

    # from django.core.mail import EmailMultiAlternatives
    #
    # subject = '突击队管理平台'
    #
    # text_content = '''如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''
    #
    # html_content = '''
    #
    #                '''
    #
    # msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    # msg.attach_alternative(html_content, "text/html")
    # msg.send()
    return HttpResponse('发送了')
