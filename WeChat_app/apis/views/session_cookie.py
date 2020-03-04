from django.http import JsonResponse
from django.views import View


class Session(View):
    def get(self, request):
        request.session['mySession'] = 'session'
        return JsonResponse({
            'key': 'value'
        })


class Cookie(View):
    def get(self, request):
        response = request.session['mySession']
        print(response)
        print(request.session.items())
        return JsonResponse({
            'key2': 'value2'
        })
