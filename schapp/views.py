# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, HttpResponseRedirect
from models import User, News
import json
import utils


def index(request):
    '首页'
    return render_to_response('schapp/index.html')


def login(request):
    '登录'
    stunum = request.GET.get('stunum', None)
    password = request.GET.get('password', None)
    users = User.objects.filter(stunum=stunum, password=password)
    if len(users) > 0:
        request.session['stunum'] = users[0].stunum
        msg = u'success:正确'
    else:
        msg = u'error:用户名或密码错误'
    print 'session:', request.session['stunum']
    return HttpResponse(msg)


def register(request):
    '注册'
    stunum = request.GET.get('stunum', None)
    password = request.GET.get('password', None)
    users = User.objects.filter(stunum=stunum)
    if len(users) == 0:  # 如果此用户名还没有被人注册
        user = User.objects.create(stunum=stunum, password=password)
        user.save()
        request.session['stunum'] = stunum  # 把用户名放入session,表示登录状态
        msg = u'success:注册成功'
        return HttpResponse(msg)
    else:
        msg = u'error:该用户名已经被注册'
        return HttpResponse(msg)


def newsList(request):
    '新闻列表'
    stunum = request.session['stunum']
    # print stunum
    if not stunum:  # 如果没有登录,就跳转到首页
        return HttpResponseRedirect('/index')
    return render_to_response('schapp/newsList.html', {'stunum': stunum})


def registerSuccess(request):
    '注册成功,中间跳转页'
    stunum = request.session['stunum']
    return render_to_response('schapp/registerSuccess.html', {'stunum': stunum})


def ajax_list(request):
    '通过ajax的方式请求和返回新闻列表'
    if request.session['stunum']:  # 已经登录
        print request.session['stunum']
        news = News.objects.all()
        # print news
        reDict = utils.get_page(news, 10, 1)
        # reDict['data_list'] = json.dumps(reDict['data_list'])
        #print reDict#['data_list']
        return HttpResponse(json.dumps(reDict), content_type='application/json')
    else:
        return HttpResponse(u'error')
