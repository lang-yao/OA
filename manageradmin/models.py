from django.db import models


# Create your models here.

class Tjd_staff(models.Model):
    name = models.CharField(default='', max_length=20, verbose_name='姓名')
    staff_id = models.CharField(default='', max_length=20, verbose_name='工号', unique=True)
    jineng = models.CharField(max_length=100, verbose_name='人员技能')
    ruzhitime = models.DateField(verbose_name='入职时间')
    fazhan = models.CharField(max_length=30, verbose_name='发展方向')
    diqu = models.CharField(default='', max_length=20, verbose_name='所在地')
    dengji = models.CharField(default='', max_length=20, verbose_name='等级')
    zhuangtai = models.IntegerField(choices=((0, '待分配'),
                                             (1, '项目中')),
                                    default=0,
                                    verbose_name='状态')

    def __str__(self):
        return "<Tjd_staff : %s>" % self.name
