from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import time, json
# Create your views here.
from django.shortcuts import redirect
# 访问限制模块 @login_required
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods

cltime = time.strftime("%Y-%m-%d", time.localtime(time.time()))


@permission_required('manager.add_xmsqd', login_url='login', raise_exception=True)
def manager_index(request):
    '''项目经理申请单计算'''
    xmjl_staff_id = request.user.staff_id
    xmsqds = User.objects.get(staff_id=xmjl_staff_id).xmsqd_set.all().count()
    xmsqds0 = User.objects.get(staff_id=xmjl_staff_id).xmsqd_set.filter(zhuangtai='0').count()
    xmsqds1 = User.objects.get(staff_id=xmjl_staff_id).xmsqd_set.filter(zhuangtai='1').count()
    return render(request, 'xmjl_index.html', {'data': xmsqds, 'data0': xmsqds0, 'data1': xmsqds1})


from .models import Xmsqd
from account.models import User


@permission_required('manager.add_xmsqd', login_url='login', raise_exception=True)
def manager_xqadd(request):
    '''需求增加模块'''
    if request.method == 'POST':
        xmname = request.POST['xmname']
        xqid = request.POST['xqid']
        xmdiqu = request.POST['xmdiqu']
        xqry = request.POST['xqry']
        ryjn = request.POST.getlist('ryjn')
        ryjn = (",".join(str(i) for i in ryjn))
        bzxx = request.POST['bzxx']
        kstime = request.POST['kstime']
        jstime = request.POST['jstime']
        xmsqd = Xmsqd()
        userid = request.session.get('_auth_user_id')
        '''获取项目组用户名称及工号'''
        xmsqd.xmname = xmname
        xmsqd.xqid = xqid
        xmsqd.xmdiqu = xmdiqu
        xmsqd.xqry = xqry
        xmsqd.ryjn = ryjn
        xmsqd.bzxx = bzxx
        xmsqd.kstime = kstime
        xmsqd.jstime = jstime
        xmsqd.xmjl_id = userid
        xmsqd.save()
        print('事件ID: 03-1', '处理时间:', cltime, '新增项目ID:', xqid, )
        return JsonResponse({'status': 'success'})
    else:
        return render(request, 'xmjl_staff_demands_add.html')


@permission_required('manager.add_xmsqd', login_url='login', raise_exception=True)
def manager_xqhistory(request):
    user_id = request.user.id
    Xmsqds = Xmsqd.objects.filter(xmjl=user_id).all()

    context = {
        'Xmsqds': Xmsqds
    }
    return render(request, 'xmjl_staff_demands_history.html', context)


@permission_required('manager.add_xmsqd', login_url='login', raise_exception=True)
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


@permission_required('manager.add_xmsqd', login_url='login', raise_exception=True)
@require_http_methods(["POST"])
def deman_access(request):
    '''评价模块'''
    data = json.loads(request.body.decode())
    id = data['id']
    access = data['access_data']
    xqaddcl = Xmsqd.objects.get(pk=id)
    old_access = json.loads(xqaddcl.access)
    for num in access.keys():
        old_access[num]['access'] = str(access[num])
    # todo 需要判断
    xqaddcl.access = json.dumps(old_access)
    xqaddcl.save()
    return JsonResponse({'status': 'success'})
