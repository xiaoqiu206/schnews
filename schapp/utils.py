# coding=utf-8
'''
Created on 2015年4月22日

@author: Administrator
'''
from django.core.paginator import Paginator
import json
from django.core.serializers import serialize


def get_page(query_set, page_num, wanted_page=1):
    '分页,query_set是没分页的数据,page_num是每页记录数,wanted_page是页数'
    page_maker = Paginator(query_set, page_num)
    re_data = {}
    re_data['page_num'] = page_num
    re_data['total_num'] = page_maker.count  # 总记录数
    re_data['total_pages'] = page_maker.num_pages  # 总页数
    re_data['wanted_page'] = wanted_page
    # print page_num, wanted_page, re_data
    wanted_page_data = page_maker.page(int(wanted_page))
    data_list = wanted_page_data.object_list
    re_data['data_list'] = serialize('json', data_list)
    re_data['page_up'] = wanted_page_data.has_previous()
    re_data['page_down'] = wanted_page_data.has_next()
    re_data['previous_page'] = int(wanted_page) - 1
    re_data['next_page'] = int(wanted_page) + 1
    # print re_data
    return re_data


def handle_zhuanti(zhuanti, news):
    if zhuanti in (u'选课', u'重修'):
        news = news.filter(title__contains=zhuanti)
    elif zhuanti == u'四六级':
        news1 = news.filter(title__contains=u'四级')
        news2 = news.filter(title__contains=u'六级')
        news = news1 | news2
    elif zhuanti == u'假期安排':
        news1 = news.filter(title__contains=u'放假')
        news2 = news.filter(title__contains=u'假期')
        news = news1 | news2
    elif zhuanti == u'期末考试':
        news = news.filter(title__contains=u'期末')
    elif zhuanti == u'比赛通知':
        news = news.filter(title__contains=u'比赛')
    elif zhuanti == u'征文活动':
        news = news.filter(title__contains=u'征文')
    return news
