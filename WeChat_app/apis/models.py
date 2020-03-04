from django.db import models


# Create your models here.
# 入口功能清单描述
class App(models.Model):
    appid = models.CharField(primary_key=True, max_length=32)  # 唯一ID
    category = models.CharField(max_length=128)  # 分类
    application = models.CharField(max_length=128)  # 功能名字
    name = models.CharField(max_length=128)  # 中文名字
    publish_date = models.DateField()  # 发布时间
    url = models.CharField(max_length=128)  # 请求链接
    desc = models.TextField()  # 描述

    def to_dict(self):
        return {
            'appid': self.appid,
            'category': self.category,
            'application': self.application,
            'name': self.name,
            'publish_date': self.publish_date,
            'url': self.url,
            'desc': self.desc
        }

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())


class User(models.Model):
    # 用户 唯一标识
    openid = models.CharField(max_length=64, unique=True)
    # 用户 昵称
    nickname = models.CharField(max_length=64)
    # 关注的城市
    focus_cities = models.TextField(default='[]')
    # 关注的星座
    focus_constellations = models.TextField(default='[]')
    # 关注的股票
    focus_stocks = models.TextField(default='[]')

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'index_'
        indexes = [
            models.Index(fields=['nickname'], name='nickname'),
            models.Index(fields=['nickname', 'openid']),
        ]
