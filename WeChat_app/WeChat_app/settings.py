"""
Django settings for WeChat_app project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd!gmbx6ou@s&9%7@@gj!mn66eos9_g7@w!q@*aj5y^++%+#kta'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apis.apps.ApisConfig',
    # 'WeChat_app.apis.apps'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'WeChat_app.urls'
USE_PROXY = False
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'WeChat_app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     },
#     # 数据库备份
#     'slave': {
#         'ENGINE': 'django.db.backends.mysql',
#         # 连接的数据库
#         'NAME': 'wechat',
#         # 用户名
#         'USER': 'root',
#         # 密码
#         'PASSWORD': '11223.',
#         # 数据库端口
#         'PORT': '3306',
#         # 连接的地址
#         'HOST': 'localhost'
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 连接的数据库
        'NAME': 'wechat',
        # 用户名
        'USER': 'root',
        # 密码
        'PASSWORD': '11223.',
        # 数据库端口
        'PORT': '3306',
        # 连接的地址
        'HOST': 'localhost'
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')
IMAGES_DIR = os.path.join(RESOURCES_DIR, 'images')

# 设置 session 过期时间
SESSION_COOKIE_AGE = 60 * 20

# 日志
LOGGING = {
    'version': 1,
    # 'disable_existing_loggers': False,
    # 格式器
    'formatters': {
        'standard': {
            'format': '%(asctime)s [ %(threadName)s: %(thread)d ] '
                      '%(pathname)s : %(funcName)s: %(lineno)d %(levelname)s - %(message)s'
        },
        'myformat': {
            'format': '%(asctime)s'
                      '%(pathname)s : %(funcName)s'
        }
    },
    # 过滤器
    'filters': {
        'xxx': {
            #    值:过滤器的路径
            '()': 'filter_No1.XXXFilter'
        }
    },
    # 持久化
    'handlers': {
        # 输出到控制台
        'console_handler': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 输出到文件
        'file_handler': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            # todo 可能需要修改
            'filename': os.path.join(BASE_DIR, 'filter_No1/log'),
            'maxBytes': 100 * 1024 * 1024,
            'backupCount': 3,
            'formatter': 'myformat',
            'encoding': 'utf-8'
        },

    },
    'loggers': {
        'django': {
            'handlers': ['console_handler', 'file_handler'],
            'filters': ['xxx'],
            'level': 'DEBUG'
        }
    }
}

# 配置缓存

CACHES = {
    'default': {
        # 1. MemCache  框架缓存
        # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        # 'LOCATION': '127.0.0.1:11211',

        # 2. DB Cache  数据库缓存
        # 'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        # 'LOCATION': 'my_cache_table',

        # 3. Filesystem Cache 文件缓存
        # 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 'LOCATION': '/var/tmp/django_cache',

        # 4. Local Mem Cache 内存缓存
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'backend-cache'
    }
}
