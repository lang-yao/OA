from django.db import models


# Create your models here.

class Xmsqd(models.Model):
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
    fpry = models.ManyToManyField('manageradmin.Tjd_staff')
    # fprystr = models.CharField(max_length=100, verbose_name='分配人员')
    xmjl = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True)
    clbz = models.CharField(max_length=100, verbose_name='处理备注')

    # def tjd_name(self):  # 创建一个作者表的方法
    #     ret = self.fpry.all()  # 查询当前对象的所有作者
    #     li = [tjd.name for tjd in ret]  # 用列表推导式将查出来的所有作者名字写入列表
    #     res = ','.join(li)  # 用逗号间隔
    #
    #     # return ','.join([author.name for author in self.authors.all()])  # 简写方式
    #
    #     return res
