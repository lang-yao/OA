from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    '''重构USER.objects'''
    # _create_user(self)受保护的方法只能这个类中调用
    def _create_user(self, staff_id, username, password, **kwargs):
        if not staff_id:
            raise ValueError('员工工号需要填写！')
        if not password:
            raise ValueError('用户密码需要填写！')
        user = self.model(staff_id=staff_id, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, staff_id, username, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(staff_id=staff_id, username=username, password=password, **kwargs)

    def create_superuser(self, staff_id, username, password, **kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(staff_id=staff_id, username=username, password=password, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    '''重构USER模型'''
    # 登陆的用户名
    username = models.CharField(max_length=20, unique=True)
    # 用户的名称
    first_name = models.CharField(max_length=30)
    # 邮箱
    email = models.CharField(max_length=30, unique=True)
    # 工号
    staff_id = models.CharField(max_length=20, unique=True)
    # 电话
    iphone = models.CharField(max_length=11, unique=True)
    # 所在地区
    diqu = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
