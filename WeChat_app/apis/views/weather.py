from django.http import HttpResponse, JsonResponse

from thirdparty import juhe
import json


def helloworld(request):
    print(' request method: ', request.method)
    print(' request META: ', request.META)
    print(' request cookies', request.COOKIES)
    m = {'message': 'Hello Django Response'}
    return JsonResponse(data=m, safe=False, status=200)


def weather(request):

    if request.method == 'GET':
        city = request.GET.get('city')
        data = juhe.weather(city)
        return JsonResponse(data=data, status=200)

    elif request.method == 'POST':
        received_dody_json = request.body
        print(received_dody_json)
        received_dody = json.loads(received_dody_json)
        cities = received_dody.get('cities')
        response_data = []
        for city in cities:
            result = juhe.weather(city)
            result['city'] = city
            response_data.append(result)
        return JsonResponse(data=response_data, status=200, safe=False)
