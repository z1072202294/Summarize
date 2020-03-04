from WeChat_app import settings
import yaml, os
import utils.response
from django.http import JsonResponse


def init_app_data():
    data_file = os.path.join(settings.BASE_DIR, 'Myappconfig.yaml')
    with open(file=data_file, mode='r', encoding='utf8') as f:
        apps = yaml.load(f, Loader=yaml.FullLoader)
        return apps


def get_menu(request):
    global_app_data = init_app_data()
    publish_app_data = global_app_data.get('publish')
    response = utils.response.wrap_json_response(data=publish_app_data,
                                                 code=utils.response.ReturnCode.SUCCESS,
                                                 )
    return JsonResponse(data=response, safe=False)
