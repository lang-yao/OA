from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tjd_staff
from django.shortcuts import redirect
from django.contrib.auth.decorators import permission_required
from account.models import User
from django.contrib.auth.models import Group, ContentType, Permission
from django.views.decorators.csrf import ensure_csrf_cookie
import time, re, json
from django.views.decorators.http import require_http_methods

# Create your views here.
# 访问限制模块 @login_required
from django.contrib.auth.decorators import login_required

cltime = time.strftime("%Y-%m-%d", time.localtime(time.time()))


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
    xmsqds = Xmsqd.objects.filter(zhuangtai='3').count()
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
@require_http_methods(["POST"])
def tjd_add(request):
    '''突击队人员添加'''
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
    res = {
        'status': 'success',
        'err': ''
    }
    print('事件ID: 01-1', '处理时间:', cltime, '创建突击队人员：', name, '-', staff_id)
    # TODO 人员添加异常
    try:
        tjd_staff.save()
    except Exception as  e:
        if e.__class__.__name__ == 'IntegrityError':
            res['err'] = re.search(r'key \'(.*)\'', str(e)).group(1)
            res['status'] = 'error'
    finally:
        if res['status'] == 'error':
            print('人员加入失败')
        print(res)
        return JsonResponse(res)


def tjd_del(id):
    '''突击队人员删除'''
    # id = request.POST['id']
    tjd_renyuan = Tjd_staff.objects.get(pk=id)
    tjd_renyuan.delete()
    # return redirect('管理员突击队模块')


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def staff_del(request):
    choice = int(request.POST.get('choice'))
    origin = request.META.get('HTTP_DEL_PATH')
    id = request.POST.get('id')
    # print(id, choice, (choice & 1))
    if origin.split('/')[2] == 'tjd_list':
        if choice & 1:
            # print('突击队人员')
            # choice为奇，表示为突击队人员删除
            tjd_del(id)
            return redirect('管理员突击队模块')
    elif origin.split('/')[2] == 'manager_user_list':
        if not choice & 1:
            # choice为偶，表示为项目经理删除
            # print('项目经理')
            manager_user_del(id)
            return redirect('管理员项目经理模块')
    else:
        return HttpResponse(request, 'wrong')


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
@require_http_methods(["POST"])
def tjd_update(request, tjd_id):
    '''突击队人员编辑'''
    tjd_renyuan = Tjd_staff.objects.get(pk=tjd_id)
    return HttpResponse(tjd_id)
    # return redirect('管理员突击队模块')


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def manager_user_list(request):
    '''项目经理列表'''
    xmjls = User.objects.filter(groups__name='项目组')
    context = {}
    context['xmjls'] = xmjls
    return render(request, 'admin_staff_xmjl.html', context)


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
@require_http_methods(["POST"])
def manager_user_add(request):
    '''项目经理人员添加'''
    if Group.objects.filter(name='项目组').first():  # 判断是否存在项目组如果不存在则创建
        print('项目组存在')
        username = request.POST['username']
        first_name = request.POST['first_name']
        staff_id = request.POST['staff_id']
        iphone = request.POST['iphone']
        email = request.POST['email']
        password = request.POST['password']
        diqu = request.POST['diqu']
        # TODO 项目经理异常
        res = {
            'status': 'success',
            'err': ''
        }
        try:
            user = User.objects.create_user(username=username, first_name=first_name, staff_id=staff_id,
                                            iphone=iphone,
                                            email=email, password=password, diqu=diqu)
            group = Group.objects.filter(name='项目组').first()  # 获取项目组
            user.groups.add(group)
            user.save()
        except Exception as  e:
            if e.__class__.__name__ == 'IntegrityError':
                res['err'] = re.search(r'key \'(.*)\'', str(e)).group(1)
                res['status'] = 'error'
        finally:
            if res['status'] == 'error':
                print('项目经理添加失败')
            else:
                print('创建项目组成功，添加成功')
                print('事件ID: 02-1', '处理时间:', cltime, '创建项目经理人员：', username, '-', staff_id)
            print(res)
            return JsonResponse(res)
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
        # TODO 项目经理异常
        res = {
            'status': 'success',
            'err': ''
        }
        try:
            user = User.objects.create_user(username=username, first_name=first_name, staff_id=staff_id,
                                            iphone=iphone,
                                            email=email, password=password, diqu=diqu)
            group = Group.objects.filter(name='项目组').first()  # 获取项目组
            user.groups.add(group)
            user.save()
        except Exception as  e:
            if e.__class__.__name__ == 'IntegrityError':
                res['err'] = re.search(r'key \'(.*)\'', str(e)).group(1)
                res['status'] = 'error'
        finally:
            if res['status'] == 'error':
                print('项目经理添加失败')
            else:
                print('创建项目组成功，添加成功')
                print('事件ID: 02-1', '处理时间:', cltime, '创建项目经理人员：', username, '-', staff_id)
            print(res)
            return JsonResponse(res)


def manager_user_del(id):
    '''项目经理人员删除'''
    xmjl_renyuan = User.objects.get(pk=id)
    xmjl_renyuan.user_permissions.clear()  # 清除权限
    xmjl_renyuan.delete()
    # return redirect('管理员项目经理模块')


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
    context = {
        'Xmsqds': Xmsqds,
        'diqus': diqus,
        'dfpry': dfpry,
    }
    return render(request, 'admin_staff_demands_add.html', context)


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
def admin_xqaddhistory(request):
    '''项目历史申请单'''

    Xmsqds = Xmsqd.objects.exclude(zhuangtai='0')

    context = {
        'Xmsqds': Xmsqds
    }

    return render(request, 'admin_staff_demands_history.html', context)


from django.conf import settings
from django.core.mail import EmailMultiAlternatives


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
@require_http_methods(["POST"])
def admin_xqaddcl(request):
    '''管理员需求单处理模块'''
    id = request.POST['id']
    zhuangtai = request.POST['zhuangtai']
    renyuanlist = request.POST.getlist('renyuanlist')
    clbz = request.POST['clbz']
    if not all(zhuangtai):
        print('没有填写')
        return redirect('新增需求模块')
    else:
        xqaddcl = Xmsqd.objects.get(pk=id)
        xqaddcl_email = xqaddcl.xmjl.email
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
        xqaddcl.zhuangtai = zhuangtai
        xqaddcl.clbz = clbz
        xqaddcl.xqcltime = cltime
        xqaddcl.save()
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
        </html>'''.format(xqaddcl.xqid, zhuangtaistr, xqaddcl.cjtime, xqaddcl.xmname, xqaddcl.kstime,
                          xqaddcl.jstime, fprystr, clbz, cltime)
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [xqaddcl_email])
        msg.attach_alternative(html_content, "text/html")
        # TODO 邮件注释
        # msg.send()
        print('事件ID: 05-1', '处理时间:', cltime, '项目ID:', id, '处理状态:', zhuangtaistr, '分配人员:', fprystr)

        return redirect('新增需求模块')


@require_http_methods(["POST"])
def admin_xqcl(request):
    id = request.POST['id']
    zhuangtai = request.POST['zhuangtai']
    jstime = request.POST['jstime']
    if zhuangtai == '3':
        zhuangtaistr = '结束-待评价'
        xqaddcl = Xmsqd.objects.get(pk=id)
        xqaddcl_email = xqaddcl.xmjl.email
        xqaddcl.zhuangtai = zhuangtai
        xqaddcl.xqcltime = cltime
        xqaddcl.jstime = cltime
        xmrys = xqaddcl.fpry.all()
        renyuanlist = []
        for xmry in xmrys:
            xmry = Tjd_staff.objects.get(staff_id=xmry.staff_id)
            renyuan = xmry.name + '-' + xmry.staff_id
            renyuanlist.append(renyuan)
            xmry.zhuangtai = '0'
            xmry.save()
        xqaddcl.save()
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
           <td style="width: 100%; max-width: 100%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
            <div class="full" style="margin: 0px auto; max-width: 600px;">
             <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
              <tbody>
               <tr>
                <td style="direction: ltr; font-size: 0px; padding-top: 0px; text-align: center; vertical-align: top;">
                 <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                  <tbody>
                   <tr>
                    <td align="center" vertical-align="middle" style="padding-top: 40px; width: 600px; background-image: url(&quot;&quot;); background-size: 100px; background-position: 10% 50%; background-repeat: no-repeat;"></td>
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
   <div tindex="2" style="margin: 0px auto; max-width: 600px;">
    <table align="center" border="0" cellpadding="0" cellspacing="0" style="background-color: rgb(255, 255, 255); background-image: url(&quot;https://www.drageasy.com/Uploads/2020/0211/e766c3e58cf27883e641a68390fb3637.png&quot;); background-repeat: no-repeat; background-size: 205px; background-position: 100% 34%;">
     <tbody>
      <tr>
       <td style="direction: ltr; font-size: 0px; text-align: center; vertical-align: top; width: 600px;">
        <table width="100%" border="0" cellpadding="0" cellspacing="0" style="vertical-align: top;">
         <tbody>
          <tr>
           <td style="width: 66.6667%; max-width: 66.6667%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
            <div class="full" style="margin: 0px auto; max-width: 600px;">
             <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 400px;">
              <tbody>
               <tr>
                <td style="direction: ltr; width: 400px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                 <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                  <tbody>
                   <tr>
                    <td align="left" style="font-size: 0px; padding: 20px 0px;">
                     <div class="text" style="font-family: &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: left; line-height: 20px; color: rgb(102, 102, 102); font-size: 14px; font-weight: normal;">
                      <div>
                       <h4><strong>项目:{} - </strong><strong style="color: rgb(230, 0, 0);">{}</strong></h4>
                      </div>
                     </div></td>
                   </tr>
                  </tbody>
                 </table></td>
               </tr>
              </tbody>
             </table>
            </div></td>
           <td style="width: 33.3333%; max-width: 33.3333%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
            <!----></td>
          </tr>
         </tbody>
        </table></td>
      </tr>
     </tbody>
    </table>
   </div>
   <div tindex="3" style="margin: 0px auto; max-width: 600px;">
    <table align="center" border="0" cellpadding="0" cellspacing="0" style="background-color: rgb(255, 255, 255); background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 1% 50%;">
     <tbody>
      <tr>
       <td style="direction: ltr; font-size: 0px; text-align: center; vertical-align: top; width: 600px;">
        <table width="100%" border="0" cellpadding="0" cellspacing="0" style="vertical-align: top;">
         <tbody>
          <tr>
           <td style="width: 50%; max-width: 50%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
            <div class="full" style="margin: 0px auto; max-width: 600px;">
             <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 300px;">
              <tbody>
               <tr>
                <td style="direction: ltr; width: 300px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                 <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                  <tbody>
                   <tr>
                    <td align="left" style="font-size: 0px; padding: 20px;">
                     <div class="text" style="font-family: &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: center; line-height: 20px; color: rgb(102, 102, 102); font-size: 14px; font-weight: normal;">
                      <div>
                       
                      </div>
                     </div></td>
                   </tr>
                  </tbody>
                 </table></td>
               </tr>
              </tbody>
             </table>
            </div></td>
           <td style="width: 50%; max-width: 50%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
            <div class="full" style="margin: 0px auto; max-width: 600px;">
             <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 300px;">
              <tbody>
               <tr>
                <td style="direction: ltr; width: 300px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                 <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                  <tbody>
                   <tr>
                    <td align="left" style="font-size: 0px; padding: 20px;">
                     <div class="text" style="font-family: &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: right; line-height: 20px; color: rgb(102, 102, 102); font-size: 14px; font-weight: normal;">
                      <div>
                       <h5>{}</h5>
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
</html>'''.format(xqaddcl.xqid, zhuangtaistr, cltime)
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [xqaddcl_email])
        msg.attach_alternative(html_content, "text/html")

        # msg.send()
        fprystr = (",".join(str(i) for i in renyuanlist))
        print('事件ID: 05-2', '处理时间:', cltime, '项目ID:', id, '处理状态:', zhuangtaistr, '释放人员:', fprystr)
        return redirect('历史需求模块')
    elif zhuangtai == '1':
        zhuangtaistr = '续期'
        xqaddcl = Xmsqd.objects.get(pk=id)
        xqaddcl_email = xqaddcl.xmjl.email
        xqaddcl.xqcltime = cltime
        xqaddcl.jstime = jstime
        xqaddcl.save()
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
                   <td style="width: 100%; max-width: 100%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
                    <div class="full" style="margin: 0px auto; max-width: 600px;">
                     <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
                      <tbody>
                       <tr>
                        <td style="direction: ltr; font-size: 0px; padding-top: 0px; text-align: center; vertical-align: top;">
                         <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                          <tbody>
                           <tr>
                            <td align="center" vertical-align="middle" style="padding-top: 40px; width: 600px; background-image: url(&quot;&quot;); background-size: 100px; background-position: 10% 50%; background-repeat: no-repeat;"></td>
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
           <div tindex="2" style="margin: 0px auto; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" style="background-color: rgb(255, 255, 255); background-image: url(&quot;https://www.drageasy.com/Uploads/2020/0211/e766c3e58cf27883e641a68390fb3637.png&quot;); background-repeat: no-repeat; background-size: 205px; background-position: 100% 34%;">
             <tbody>
              <tr>
               <td style="direction: ltr; font-size: 0px; text-align: center; vertical-align: top; width: 600px;">
                <table width="100%" border="0" cellpadding="0" cellspacing="0" style="vertical-align: top;">
                 <tbody>
                  <tr>
                   <td style="width: 66.6667%; max-width: 66.6667%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
                    <div class="full" style="margin: 0px auto; max-width: 600px;">
                     <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 400px;">
                      <tbody>
                       <tr>
                        <td style="direction: ltr; width: 400px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                         <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                          <tbody>
                           <tr>
                            <td align="left" style="font-size: 0px; padding: 20px 0px;">
                             <div class="text" style="font-family: &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: left; line-height: 20px; color: rgb(102, 102, 102); font-size: 14px; font-weight: normal;">
                              <div>
                               <h4><strong>项目:{} - </strong><strong style="color: rgb(230, 0, 0);">{} 至 {}</strong></h4>
                              </div>
                             </div></td>
                           </tr>
                          </tbody>
                         </table></td>
                       </tr>
                      </tbody>
                     </table>
                    </div></td>
                   <td style="width: 33.3333%; max-width: 33.3333%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
                    <!----></td>
                  </tr>
                 </tbody>
                </table></td>
              </tr>
             </tbody>
            </table>
           </div>
           <div tindex="3" style="margin: 0px auto; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" style="background-color: rgb(255, 255, 255); background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 1% 50%;">
             <tbody>
              <tr>
               <td style="direction: ltr; font-size: 0px; text-align: center; vertical-align: top; width: 600px;">
                <table width="100%" border="0" cellpadding="0" cellspacing="0" style="vertical-align: top;">
                 <tbody>
                  <tr>
                   <td style="width: 50%; max-width: 50%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
                    <div class="full" style="margin: 0px auto; max-width: 600px;">
                     <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 300px;">
                      <tbody>
                       <tr>
                        <td style="direction: ltr; width: 300px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                         <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                          <tbody>
                           <tr>
                            <td align="left" style="font-size: 0px; padding: 20px;">
                             <div class="text" style="font-family: &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: center; line-height: 20px; color: rgb(102, 102, 102); font-size: 14px; font-weight: normal;">
                              <div>

                              </div>
                             </div></td>
                           </tr>
                          </tbody>
                         </table></td>
                       </tr>
                      </tbody>
                     </table>
                    </div></td>
                   <td style="width: 50%; max-width: 50%; min-height: 1px; font-size: 13px; text-align: left; direction: ltr; vertical-align: top; padding: 0px;">
                    <div class="full" style="margin: 0px auto; max-width: 600px;">
                     <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 300px;">
                      <tbody>
                       <tr>
                        <td style="direction: ltr; width: 300px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                         <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                          <tbody>
                           <tr>
                            <td align="left" style="font-size: 0px; padding: 20px;">
                             <div class="text" style="font-family: &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: right; line-height: 20px; color: rgb(102, 102, 102); font-size: 14px; font-weight: normal;">
                              <div>
                               <h5>{}</h5>
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
        </html>'''.format(xqaddcl.xqid, zhuangtaistr, jstime, cltime)
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [xqaddcl_email])
        msg.attach_alternative(html_content, "text/html")
        # msg.send()
        return redirect('历史需求模块')
    else:
        return redirect('历史需求模块')


@permission_required(['account.change_user', 'account.add_user', 'account.view_user', 'account.delete_user',
                      'manageradmin.change_tjd_staff', 'manageradmin.delete_tjd_staff', 'manageradmin.add_tjd_staff',
                      'manageradmin.view_tjd_staff', 'manager.view_xmsqd', 'manager.change_xmsqd'], login_url='login',
                     raise_exception=True)
@require_http_methods(["POST"])
def query_demand_staff(request):
    '''人员查询模块'''
    id = request.POST['id']
    xqaddcl = Xmsqd.objects.get(pk=id)
    access = xqaddcl.access
    data = {}
    if access != '':
        access = json.loads(access, strict=False)
        for i in xqaddcl.fpry.all():
            data[i.staff_id] = {
                "name": i.name,
                "access": access[i.staff_id]['access']
            }
    else:
        for i in xqaddcl.fpry.all():
            data[i.staff_id] = {
                "name": i.name,
                "access": ""
            }
        xqaddcl.access = json.dumps(data)
        xqaddcl.save()
    print(data)
    return JsonResponse(data)
# def query_demand_staff(request):
#     '''人员查询模块'''
#     id = request.POST['id']
#     xqaddcl = Xmsqd.objects.get(pk=id)
#     access = json.loads(xqaddcl.access)
#     data = {}
#     for i in xqaddcl.fpry.all():
#         data[i.staff_id] = {
#             'name': i.name,
#             'access': access[i.staff_id]
#         }
#     print(data)
#     return JsonResponse(data)
