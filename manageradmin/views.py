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
        jineng = (",".join(str(i) for i in jineng))
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
def manager_user_list(request):
    '''项目经理列表'''
    xmjls = User.objects.filter(groups__name='项目组')
    # for i in xmjls:
    #     print('项目组用户:',i.username)
    #     print('用户名称:',i.first_name)
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
    # id = 4
    id = request.POST['id']
    xmjl_renyuan = User.objects.get(id=id)
    xmjl_renyuan.user_permissions.clear()  # 清除权限
    xmjl_renyuan.delete()
    return redirect('管理员项目经理模块')


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def manager_user_update(request):
    '''项目经理人员更新'''
    pass


from manager.models import Xmsqd
from collections import defaultdict


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def admin_xqadd(request):
    '''管理员项目总需求列表，获取待处理的订单'''
    Xmsqds = Xmsqd.objects.filter(zhuangtai='0').values('id', 'xqid', 'xmname', 'cjtime', 'xmjl', 'xmjl__first_name',
                                                        'xmjl__staff_id', 'kstime', 'jstime', 'xmdiqu', 'xqry', 'ryjn',
                                                        'bzxx')

    # print(Xmsqds)
    #
    # first_name = {}
    # print('正向查询-------')
    # for i in Xmsqds:
    #     xmjl = Xmsqd.objects.get(pk=i.id)
    #     aa =xmjl.xmjl.all()
    #     for i in aa:
    #         print(i.first_name)

    # print(first_name)
    # print(a)

    # print('反向查询-------')
    # aaaa = User.objects.get(pk=2)
    # print(aaaa.xmsqd_set.all().values('xqid'))

    # Xmsqds1 = Xmsqd.objects.get(pk=1)
    # print(Xmsqds1)
    # a = Xmsqds1.xmjl.all()
    # for i in a:
    #     print(i.first_name)

    '''获取未分配的人员地区进行去重'''
    diqus = Tjd_staff.objects.filter(zhuangtai='0').values('diqu').distinct()
    dfpry = defaultdict(list)
    '''获取未分配的地区及人员'''
    for i in diqus:
        dfpry[i['diqu']]
        dqry = Tjd_staff.objects.filter(zhuangtai='0').filter(**i)
        for name in dqry:
            dfpry[i['diqu']].append(name.name + '-' + name.staff_id)
            # print(name.name)
    dfpry = dict(dfpry)
    # print(dfpry)
    context = {
        'Xmsqds': Xmsqds,
        'diqus': diqus,
        'dfpry': dfpry,
    }
    # print(context['dfpry'])

    # for k ,v in dfpry.items():
    #     print(k)
    #     for i in v :
    #         print(i)

    # context = {
    #     'Xmsqds': Xmsqds,
    #     'diqus': diqus,
    # }
    return render(request, 'admin_staff_demands_add.html', context)


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def admin_xqaddhistory(request):
    '''项目历史申请单'''

    # Xmsqds = Xmsqd.objects.values('id', 'xqid', 'xmname', 'zhuangtai', 'cjtime', 'xmjl__first_name', 'xmjl__staff_id',
    #                               'kstime', 'jstime', 'xmdiqu', 'xqry', 'ryjn', 'bzxx', 'clbz', 'fpry__name')

    Xmsqds = Xmsqd.objects.all()
    context = {
        'Xmsqds': Xmsqds
    }

    return render(request, 'admin_staff_demands_history.html', context)


from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import time


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def admin_xqaddcl(request):
    '''管理员需求单处理模块'''
    if request.method == 'POST':
        id = request.POST['id']
        zhuangtai = request.POST['zhuangtai']
        renyuanlist = request.POST.getlist('renyuanlist')
        clbz = request.POST['clbz']
        if not all(zhuangtai):
            print('没有填写')
            return redirect('新增需求模块')
        else:
            xqaddcl = Xmsqd.objects.get(id=id)
            xqaddcl_email = xqaddcl.xmjl
            if zhuangtai == '1':
                zhuangtaistr = '受理'
                for renyuan in renyuanlist:
                    staff_id = renyuan.split("-", 1)[1]
                    tjdry = Tjd_staff.objects.get(staff_id=staff_id)
                    xqaddcl.fpry.add(tjdry)
                    tjdry.zhuangtai = '1'
                    tjdry.save()
            else:
                zhuangtaistr = '驳回'
            fprystr = (",".join(str(i) for i in renyuanlist))
            print(fprystr)
            xqaddcl.zhuangtai = zhuangtai
            xqaddcl.clbz = clbz
            xqaddcl.fprystr = fprystr
            xqaddcl.save()
            xqaddclxx_xqcltime = time.strftime('%Y/%m/%d', time.localtime(time.time()))

            subject = '突击队管理平台'
            text_content = '''如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''
            html_content = '''<html>
 <head>
  <meta charset="utf-8" />
 </head>
 <body>
  <div class="content-wrap" style="margin: 0px auto; overflow: hidden; padding: 0px; border: 0px dotted rgb(238, 238, 238); width: 600px;">
   <!---->
   <div tindex="1" style="margin: 0px auto; max-width: 600px;">
    <table align="center" border="0" cellpadding="0" cellspacing="0" style="background-color: rgb(255, 255, 255); background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 1% 50%;">
     <tbody>
      <tr>
       <td style="direction: ltr; font-size: 0px; text-align: center; vertical-align: top; width: 600px;">
        <table width="100%" border="0" cellpadding="0" cellspacing="0" style="vertical-align: top;">
         <tbody>
          <tr>
           <td style="width: 40%; max-width: 40%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
            <div class="full" style="margin: 0px auto; max-width: 600px; line-height: 0px;">
             <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 240px;">
              <tbody>
               <tr>
                <td align="center" style="direction: ltr; font-size: 0px; padding: 25px 0px; text-align: center; vertical-align: top; word-break: break-word; width: 240px; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                 <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse: collapse; border-spacing: 0px;">
                  <tbody>
                   <tr>
                    <td style="width: 375px; border-top: 1px solid rgb(204, 204, 204);"></td>
                   </tr>
                  </tbody>
                 </table></td>
               </tr>
              </tbody>
             </table>
            </div></td>
           <td style="width: 20%; max-width: 20%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
            <div class="full" style="margin: 0px auto; max-width: 600px;">
             <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 120px;">
              <tbody>
               <tr>
                <td style="direction: ltr; width: 120px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                 <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                  <tbody>
                   <tr>
                    <td align="left" style="font-size: 0px; padding: 13px 20px;">
                     <div class="text" style="font-family: &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: center; line-height: 20px; color: rgb(51, 51, 51); font-size: 16px; font-weight: bolder;">
                      <div>
                       <h3 style="line-height: 24px; font-size: 1.17em; font-weight: bold; margin: 0px;"><strong>处理结果</strong><span class="ql-cursor">﻿</span></h3>
                      </div>
                     </div></td>
                   </tr>
                  </tbody>
                 </table></td>
               </tr>
              </tbody>
             </table>
            </div></td>
           <td style="width: 40%; max-width: 40%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
            <div class="full" style="margin: 0px auto; max-width: 600px; line-height: 0px;">
             <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 240px;">
              <tbody>
               <tr>
                <td align="center" style="direction: ltr; font-size: 0px; padding: 25px 0px; text-align: center; vertical-align: top; word-break: break-word; width: 240px; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                 <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse: collapse; border-spacing: 0px;">
                  <tbody>
                   <tr>
                    <td style="width: 375px; border-top: 1px solid rgb(204, 204, 204);"></td>
                   </tr>
                  </tbody>
                 </table></td>
               </tr>
              </tbody>
             </table>
            </div></td>
          </tr>
         </tbody>
        </table></td>
      </tr>
     </tbody>
    </table>
   </div>
   <div class="full" tindex="2" style="margin: 0px auto; max-width: 600px;">
    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
     <tbody>
      <tr>
       <td style="direction: ltr; width: 600px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
        <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
         <tbody>
          <tr>
           <td align="left" style="font-size: 0px; padding: 4px 7px;">
            <div class="text" style="font-family: &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: left; line-height: 20px; color: rgb(102, 102, 102); font-size: 12px; font-weight: normal;">
             <div>
              <h3 style="line-height: 24px; font-size: 1.17em; font-weight: bold; margin: 0px;"><span style="color: rgb(230, 0, 0);">{} - {}</span></h3>
             </div>
            </div></td>
          </tr>
         </tbody>
        </table></td>
      </tr>
     </tbody>
    </table>
   </div>
   <div class="full" tindex="3" style="margin: 0px auto; max-width: 600px;">
    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
     <tbody>
      <tr>
       <td style="direction: ltr; width: 600px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;https://www.drageasy.com/Uploads/2020/0211/e766c3e58cf27883e641a68390fb3637.png&quot;); background-repeat: no-repeat; background-size: 254px; background-position: 100% 9%;">
        <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
         <tbody>
          <tr>
           <td align="left" style="font-size: 0px; padding: 20px;">
            <div class="text" style="font-family: &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: left; line-height: 12px; color: rgb(102, 102, 102); font-size: 12px; font-weight: normal;">
             <div>
              <p style="text-size-adjust: none; word-break: break-word; line-height: 12px; font-size: 12px; margin: 0px;">申请时间：{}</p>
              <p style="text-size-adjust: none; word-break: break-word; line-height: 12px; font-size: 12px; margin: 0px;">项目名称：{}</p>
                <p style="text-size-adjust: none; word-break: break-word; line-height: 12px; font-size: 12px; margin: 0px;">支撑时间：{} - {}</p>
              <p style="text-size-adjust: none; word-break: break-word; line-height: 12px; font-size: 12px; margin: 0px;">分配人员：{}</p>
              <p style="text-size-adjust: none; word-break: break-word; line-height: 12px; font-size: 12px; margin: 0px;">备注信息：{}</p>
             </div>
            </div></td>
          </tr>
         </tbody>
        </table></td>
      </tr>
     </tbody>
    </table>
   </div>
   <div tindex="4" style="margin: 0px auto; max-width: 600px;">
    <table align="center" border="0" cellpadding="0" cellspacing="0" style="background-color: rgb(255, 255, 255); background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 1% 50%;">
     <tbody>
      <tr>
       <td style="direction: ltr; font-size: 0px; text-align: center; vertical-align: top; width: 600px;">
        <table width="100%" border="0" cellpadding="0" cellspacing="0" style="vertical-align: top;">
         <tbody>
          <tr>
           <td style="width: 25%; max-width: 25%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
            <!----></td>
           <td style="width: 25%; max-width: 25%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
            <!----></td>
           <td style="width: 25%; max-width: 25%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
            <!----></td>
           <td style="width: 25%; max-width: 25%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
            <div class="full" style="margin: 0px auto; max-width: 600px;">
             <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 150px;">
              <tbody>
               <tr>
                <td style="direction: ltr; width: 150px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                 <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                  <tbody>
                   <tr>
                    <td align="left" style="font-size: 0px; padding: 20px;">
                     <div class="text" style="font-family: &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: center; line-height: 20px; color: rgb(102, 102, 102); font-size: 14px; font-weight: normal;">
                      <div>
                       <p style="text-size-adjust: none; word-break: break-word; line-height: 20px; font-size: 14px; margin: 0px;">{}</p>
                      </div>
                     </div></td>
                   </tr>
                  </tbody>
                 </table></td>
               </tr>
              </tbody>
             </table>
            </div></td>
          </tr>
         </tbody>
        </table></td>
      </tr>
     </tbody>
    </table>
   </div>
  </div>
 </body>
</html>''' \
                # .format(xqaddcl.xqid,zhuangtaistr,xqaddcl.cjtime,xqaddcl.xmname,xqaddcl.kstime,xqaddcl.jstime,fpry,clbz,xqaddclxx_xqcltime)
            # msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [xqaddcl_email])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            return redirect('新增需求模块')
    else:
        return redirect('新增需求模块')

# @permission_required(['account.change_user','account.add_user','account.view_user','account.delete_user','manageradmin.change_tjd_staff','manageradmin.delete_tjd_staff','manageradmin.add_tjd_staff','manageradmin.view_tjd_staff','manager.view_xmsqd','manager.change_xmsqd'],login_url='login',raise_exception=True)
# def admin_xqaddcl(request):
#     if request.method == 'POST':
#         # xqid = request.POST['xqid']
#         zhuangtai = request.POST['zhuangtai']
#         renyuanlist = request.POST.getlist('renyuanlist')
#         fpry = (",".join(str(i) for i in renyuanlist))
#         clbz = request.POST['clbz']
#         print(renyuanlist)
#         print(zhuangtai,clbz)
#         xqaddcl = Xmsqd.objects.get(xqid='A0000000')
#         xqaddcl.zhuangtai=zhuangtai
#         xqaddcl.clbz = clbz
#         xqaddcl.fpry = fpry
#         xqaddcl.save()
#         return redirect('新增需求模块')
#     else:
#         return redirect('新增需求模块')
