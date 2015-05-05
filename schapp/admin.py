# coding=utf-8
from django.contrib import admin
from models import User, News, Department
import constants


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'stunum', 'department', 'reg_time')
    ording = ('-createTime',)
    list_per_page = constants.ADMIN_LIST_PER_PAGE
    list_filter = ('reg_time', 'department')
    search_fields = ['stunum']


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'section', 'links', 'type', 'rel_time')
    ording = ('-rel_time',)
    list_filter = ('type',)
    list_per_page = constants.ADMIN_LIST_PER_PAGE
    search_fields = ['title']


class InterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ording = ('id',)
    list_per_page = constants.ADMIN_LIST_PER_PAGE


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ording = ('id',)
    list_per_page = constants.ADMIN_LIST_PER_PAGE


admin.site.register(User, UserAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Department, DepartmentAdmin)
