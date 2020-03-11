import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeChat_app.settings')
django.setup()

import logging


def log_demo():
    logger = logging.getLogger('django')
    logger.info('我是 info log')
    logger.info('我是 info log zjt')
    # warning
    logger.warning('我是 warning log')
    logger.warning('我是 warning log zjt')
    # error
    logger.error('我是 error log')
    logger.error('我是 error log zjt')


if __name__ == '__main__':
    log_demo()
