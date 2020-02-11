# 访问限制模块 @login_required
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Tjd_staff


@login_required
def tjd_index(request):
    # 突击队人员总数
    tjds = Tjd_staff.objects.all().count()
    print(tjds)
    # 已分配的突击队人员总数
    tjds1 = Tjd_staff.objects.filter(zhuangtai=0).count()
    # 未分配的突击队人员总数
    tjds0 = Tjd_staff.objects.filter(zhuangtai=1).count()
    return render(request, 'admin_index.html', {'data': tjds, 'data1': tjds1, 'data0': tjds0})


@login_required
def tjd_list(request):
    tjds = Tjd_staff.objects.all()
    context = {}
    context['tjds'] = tjds
    return render(request, 'admin_staff_tjd.html', context)


@login_required
def tjd_add(request):
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


def tjd_del(request):
    id = request.POST['id']
    print(id)
    # tjd_renyuan = Tjd_staff.objects.get(staff_id=)
    # tjd_renyuan.delete()
    return HttpResponse('success')


def xmjl(request):
    return render(request, 'xmjl_staff_demands_add.html')
