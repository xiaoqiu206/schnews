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
        if 'date' in request.GET:
            date = request.GET['date']
            startDate = date.split('--')[0]
            endDate = date.split('--')[1]
            # print startDate, endDate
            news = news.filter(rel_time__gte=startDate)  # 大于等于开始日期
            news = news.filter(rel_time__lte=endDate)  # 小于等于结束日期
        # 加len(news) >0 的原因是,如果之前过滤后就没有数据了,其他条件就不用过滤了
        if len(news) > 0 and 'key_word' in request.GET:
            keyword = request.GET['key_word']
            news = news.filter(title__contains=keyword)
        if len(news) > 0 and 'department' in request.GET:
            department = request.GET['department']
            news = news.filter(section=department)
        if len(news) > 0 and 'zhuanti' in request.GET:
            zhuanti = request.GET['zhuanti']
            news = utils.handle_zhuanti(zhuanti, news)
        reDict = utils.get_page(news, 10, request.GET['page'])
        # reDict['data_list'] = json.dumps(reDict['data_list'])
        # print reDict#['data_list']
        return HttpResponse(json.dumps(reDict), content_type='application/json')
    else:
        return HttpResponse(u'error')
