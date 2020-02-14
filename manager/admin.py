from django.contrib import admin
from .models import Xmsqd


@admin.register(Xmsqd)
class XmsqdAdmin(admin.ModelAdmin):
    list_display = (
    "id", "xmjl_first_name", "xmjl_staff_id", "xqid", "xmname", "xmdiqu", "xqry", "ryjn", "bzxx", "kstime", "jstime",
    "cjtime", "zhuangtai", "fpry", "clbz")
    # 排序 正序 ordering = ("id",) 倒序 ordering = ("-id",)
    ordering = ("id",)
