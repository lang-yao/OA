from django.contrib import admin
from .models import Tjd_staff
# Register your models here.

@admin.register(Tjd_staff)
class Tjd_staffAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "staff_id", "jineng", "ruzhitime", "fazhan", "diqu", "dengji", "zhuangtai")
    # 排序 正序 ordering = ("id",) 倒序 ordering = ("-id",)
    ordering = ("id",)

# admin.site.register(Tjd_staff, Tjd_staffAdmin)
