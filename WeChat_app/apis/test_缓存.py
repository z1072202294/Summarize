import os
import django
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeChat_app.settings')
django.setup()
from django.core.cache import cache


def get():
    time.sleep(5)
    res = cache.get('可乐')
    print(res)


if __name__ == '__main__':
    cache.set('可乐','百事可乐',5)
    print(cache.get('可乐'))
    get()
