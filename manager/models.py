from django.db import models

# Create your models here.

class Xmsqd(models.Model):
    xmjl_first_name = models.CharField(max_length=20, verbose_name='项目经理名称')
    xmjl_staff_id = models.CharField(max_length=20, verbose_name='项目经理工号')
    xqid = models.CharField(max_length=20, verbose_name='需求编号')
    xmname = models.CharField(max_length=20, verbose_name='项目名称')
    xmdiqu = models.CharField(max_length=10, verbose_name='需求地区')
    xqry = models.CharField(max_length=10, verbose_name='所需人数')
    ryjn = models.CharField(max_length=50, verbose_name='人员技能')
    bzxx = models.CharField(max_length=100, verbose_name='备注信息')
    kstime = models.DateField(verbose_name='开始时间')
    jstime = models.DateField(verbose_name='结束时间')
    cjtime = models.DateField(auto_now_add=True, verbose_name='创建时间')
    zhuangtai = models.IntegerField(choices=((0, '待审核'),
                                             (1, '受理'),
                                             (2, '驳回')),
                                    default=0,
                                    verbose_name='状态')
    fpry = models.CharField(max_length=50, verbose_name='分配人员')
    clbz = models.CharField(max_length=100, verbose_name='处理备注')

    def __str__(self):
        return "<Xmsqd : %s>" % self.xmname
