# coding=utf-8
from django.db import models


class News(models.Model):
    '新闻'
    title = models.CharField(u'新闻标题', max_length=500)
    rel_time = models.CharField(u'发布时间', max_length=30)
    section = models.CharField(u'发布部门', max_length=30)
    links = models.CharField(u'正文链接', max_length=500)
    type = models.CharField(u'栏目', max_length=30)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'新闻'
        verbose_name_plural = u'新闻'


class User(models.Model):
    '用户'
    stunum = models.CharField(u'学号', max_length=30)
    password = models.CharField(u'密码', max_length=20)
    department = models.ForeignKey('Department', verbose_name=u'部门', null=True, blank=True)
    reg_time = models.DateTimeField(u'注册时间', auto_now_add=True, null=True, blank=True)

    def __unicode__(self):
        return self.stunum

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户'


class Department(models.Model):
    '部门'
    name = models.CharField(u'部门', max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = u'部门'
