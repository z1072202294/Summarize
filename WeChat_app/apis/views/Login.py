from django.http import JsonResponse, HttpResponse
from django.views import View
import json, requests
from utils.app_key import *
from apis.models import User

class Authorize(View):
    def get(self, request):
        print(request.COOKIES)
        return HttpResponse(request.GET)

    def post(self, request):
        # print('获取微信发来的code : ', request.body)  # b'{"code":"033Bucsb0noMFx1uidsb0WYwsb0Bucs4"}'
        code_str = request.body.decode('utf-8')
        # print(code_str)
        code_dict = json.loads(code_str)
        nickname=code_dict.get('nickname')
        code = code_dict.get('code')
        # print('解码后的 code: ', code)
        # appid 微信小程序 的AppID
        # secret 微信小程序的 AppSecret
        # js_code 微信发送给后台的 code
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' \
              % (AppID, AppSecret, code)
        response = requests.get(url=url)
        # print('获取到 "session_key" 与 "openid" : ', response.text)
        # print(type(response.text))
        authorize_dict = json.loads(response.text)
        openid = authorize_dict.get('openid')
        if not openid:
            return HttpResponse('Authorize fail')

        # 给这个用户赋予一些状态
        request.session['openid'] = openid
        request.session['is_authorized'] = True
        # 将用户保存到 数据库
        if not User.objects.filter(openid=openid):
            newuser = User(openid=openid,nickname=nickname)
            newuser.save()


        return HttpResponse('Authorize post ok')




