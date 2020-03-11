from logging import Filter
class XXXFilter(Filter):
    def filter(self, record):
        # 带什么不用输出
        if 'zjt' in record.msg:
            return False
        return True