import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeChat_app.settings')
django.setup()

from apis.models import User, App
import random


def ranstr(length):
    CHS = 'ASDFGHJKLZXCVBNMQWERTYUIOPqwertyuiopasdfghjklzxcvbnm'
    salt = ''
    for i in range(length):
        salt += random.choice(CHS)
    return salt


# 添加一个用户
def add_one():
    # 1
    user = User(openid='test_openid_1', nickname='test_nickname_1')
    user.save()
    # 2
    User.objects.create(openid='test_openid_2', nickname='test_nickname_2')


# 增 : 批量添加
def add_batch():
    # bulk_create 批量添加数据
    new_user_list = []
    for i in range(10):
        openid = ranstr(32)
        nickname = ranstr(10)
        user = User(openid=openid, nickname=nickname)
        new_user_list.append(user)
    User.objects.bulk_create(new_user_list)


# 查询一个用户
def get_one():
    user = User.objects.get(openid='test_openid_1')
    print(user)


# 数据过滤
def get_filter():
    users = User.objects.filter(openid__contains='test_')
    print(users)


# 数据排序
def get_order():
    users = User.objects.order_by('openid')
    print(users)


# 连锁查询
def get_chain():
    users = User.objects.filter(openid__contains='test_').order_by('openid')
    print(users)


# 改一个
def modify_one():
    user = User.objects.get(openid='test_openid_1')
    user.nickname = 'modify_nickname'
    user.save()


# 改: 批量改
def modify_batch():
    User.objects.filter(openid__contains='test_').update(nickname='modify_username')


# 删除一个
def delete_one():
    User.objects.get(openid='test_openid_1').delete()


# 删除 : 批量删除
def delete_batch():
    User.objects.filter(openid__contains='test_').delete()


# 全部删除
def delete_all():
    User.objects.all().delete()
    # 这个语法不能用
    # User.objects.delete()


# ---------------------------------------------

# 数据库操作函数

#  1. 字符串操作函数

# 字符串的拼接 : Concat

from django.db.models.functions import Concat
from django.db.models import Value


def concat_function():
    # annotate 定义这个模型里面没有的变量 并且需要输出
    user = User.objects.filter(openid='test_openid_1').annotate(
        screen_name=Concat(
            Value('openid='),
            'openid',
            Value(','),
            Value('nickname='),
            'nickname')
    )[0]
    print('screen_name = ', user.screen_name)


# 字符串长度 : Length

from django.db.models.functions import Length


def length_function():
    user = User.objects.filter(openid='test_openid_1').annotate(
        openid_length=Length('openid'))[0]
    print(user.openid_length)


# 字符串大小写函数
from django.db.models.functions import Upper, Lower


def case_function():
    user = User.objects.filter(openid='test_openid_1').annotate(
        upper_openid=Upper('openid'),
        lower_openid=Lower('openid')
    )[0]
    print('upper_openid : ', user.upper_openid, 'lower_openid :', user.lower_openid)


#  2. 日期处理函数

from django.db.models.functions import Now


# NOW() 获取当前时间
def now_function():
    # 返回当前日期之前所有的app应用
    apps = App.objects.filter(publish_date__lte=Now())
    for app in apps:
        print(app)


# 时间截断函数 Trunc
from django.db.models import Count
from django.db.models.functions import Trunc
from django.db.models.query import QuerySet


def trunc_function():
    # 打印每一天发布的应用数量
    app_per_day = App.objects.annotate(
        #                                 day month year
        publish_day=Trunc('publish_date', 'month')) \
        .values('publish_day') \
        .annotate(publish_num=Count('appid'))
    for app in app_per_day:
        print(app['publish_day'], app['publish_num'])


if __name__ == '__main__':
    trunc_function()
