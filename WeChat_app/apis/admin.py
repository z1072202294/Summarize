from django.contrib import admin
from apis.models import User, App
import time

# Register your models here.

admin.site.register(App)


# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 不想显示的内容

    exclude = ['openid'] # 与 include 相反 , 不显示 xx属性
    #  定义一些规则来控制后台插入模型字段的值

    def save_model(self, request, obj, form, change):
        print('KKK', obj)
        obj.openid = obj.nickname + str(time.time())

        return super(UserAdmin, self).save_model(request, obj, form, change)
