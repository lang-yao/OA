from django.db import models


# Create your models here.

class Xmsqd(models.Model):
    xqid = models.CharField(max_length=20, verbose_name='需求编号')
    xmname = models.CharField(max_length=20, verbose_name='项目名称')
    xmdiqu = models.CharField(max_length=10, verbose_name='需求地区')
    xqry = models.CharField(max_length=10, verbose_name='所需人数')
    ryjn = models.CharField(max_length=50, verbose_name='人员技能')
    bzxx = models.CharField(max_length=100, verbose_name='备注信息')
    kstime = models.DateField(blank=True, default=None, verbose_name='开始时间')
    jstime = models.DateField(blank=True, default=None, verbose_name='结束时间')
    cjtime = models.DateField(auto_now_add=True, verbose_name='创建时间')
    xqcltime = models.DateField(blank=True, default=None, null=True, verbose_name='需求处理时间')
    zhuangtai = models.IntegerField(choices=((0, '待审核'),
                                             (1, '受理'),
                                             (2, '驳回'),
                                             (3, '待评价'),
                                             (4, '完成'),
                                             ),
                                    default=0,
                                    verbose_name='状态')
    fpry = models.ManyToManyField('manageradmin.Tjd_staff')
    xmjl = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True)
    clbz = models.CharField(max_length=100, verbose_name='处理备注')
    access = models.TextField(verbose_name='人员评价')
