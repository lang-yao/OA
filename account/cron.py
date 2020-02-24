#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@author: 4rat
@time: 2020/2/18 18:14
"""
from manager.models import Xmsqd
from manageradmin.models import Tjd_staff
import time

def renwu():
    dqtime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    xms = Xmsqd.objects.filter(zhuangtai='1').all()
    for i in xms:
        xmid = i.id
        xm = Xmsqd.objects.get(id=xmid)
        xmjstime = str(i.jstime)
        if dqtime >= xmjstime:
            print('当前日期：', dqtime, '项目ID', xmid, xmjstime, '结束', '已到期！')
            xm.zhuangtai = 3
            xm.save()
            tjdrys = i.fpry.all()
            for ry in tjdrys:
                tjdryid = ry.id
                tjdry = Tjd_staff.objects.get(id=tjdryid)
                tjdry.zhuangtai = 0
                print('人员ID', tjdryid, ry.name, '已经释放')
                print('*' * 20)
                tjdry.save()
        else:
            print('当前日期：', dqtime, '项目ID', xmid, xmjstime, '结束', '未到期！')
            print('*' * 30)
