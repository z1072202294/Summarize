from django.http import JsonResponse, HttpResponse
from django.views import View
from .auth import already_authorized
import json,requests
from apis.models import User
class Logout(View):
    def get(self, request):
        print(request.session.items())
        request.session.clear()
        return JsonResponse({
            'key': 'logout ok'
        }, safe=False)


class Status(View):
    def get(self, request):
        print(request.session.items())
        if already_authorized(request):
            data = {'is_authorized': 1}
        else:
            data = {'is_authorized': 0}
        return JsonResponse(data=data, safe=False)

# def weather(cityname):
#     '''
#     :param cityname: 城市名字
#     :return: 返回实况天气
#     '''
#     print('----------->',cityname[:-1])
#     key = 'c8fc9a2cd8831b4b862c717064fbd79a'
#     api = 'http://apis.juhe.cn/simpleWeather/query'
#     params = 'cityname=%s&key=%s' % (cityname[:-1], key)
#     url = api + '?' + params
#     print(url)
#     response = requests.get(url=url)
#     data = json.loads(response.text)
#     print(data)
#     result = data.get('result')
#     realtime = result.get('realtime')
#     response = {}
#     response['temperature'] = realtime.get('temperature')
#     response['wid'] = realtime.get('wid')
#     response['power'] =  realtime.get('power')
#     response['humidity'] = realtime.get('humidity')
#     return response
def weather(CityName):
    """
    :param CityName: 城市名字
    :return: 返回实时天气
    """
    key = 'c8fc9a2cd8831b4b862c717064fbd79a'
    api = 'http://v.juhe.cn/weather/index'
    params = 'cityname=%s&key=%s' % (CityName, key)
    url = api + '?' + params
    # print(url)
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    # print(json_data)
    result = json_data.get('result')
    sk = result.get('sk')
    response = dict()
    response['temperature'] = sk.get('temp')  # 天气
    response['wid'] = sk.get('wind_direction')  # 风向
    response['power'] = sk.get('wind_strength')  # 风的强度
    response['humidity'] = sk.get('humidity')  # 湿度
    # response['time'] = sk.get('time')  # 当前时间
    print(response)
    return response

class Weather(View):
    def get(self, request):
        if not already_authorized(request):
            response = {'key':2500}
        else:
            data = []
            openid = request.session.get('openid')
            user = User.objects.filter(openid=openid)[0]
            cities = json.loads(user.focus_cities)
            for city in cities:
                result = weather(city.get('city'))
                result['city_info'] = city
                data.append(result)
            response = data
        return JsonResponse(data=response, safe=False)
        pass

    def post(self, request):
        data = []
        received_body = request.body.decode('utf-8')
        received_body = json.loads(received_body)
        print(received_body)
        cities = received_body.get('cities')
        for city in cities:
            result = weather(city.get('city'))
            result['city_info'] = city
            data.append(result)
        response_data = {'key':'post..'}
        return JsonResponse(data=response_data, safe=False)