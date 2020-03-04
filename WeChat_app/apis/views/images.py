from django.http import HttpResponse, FileResponse, Http404, JsonResponse
import os, utils, hashlib
from WeChat_app.settings import BASE_DIR, IMAGES_DIR
from django.views import View


# def get_image(request):
#     FilePath = os.path.join(BASE_DIR, 'images', 'timg.jpg')
#     with open(file=FilePath, mode='rb') as f:
#         return HttpResponse(content=f, content_type='image/png')
#         # return FileResponse(content=f, content_type='image/png')
#
#
# class ImageView(View):
#     def get(self, request):
#         FilePath = os.path.join(BASE_DIR, 'images', 'timg.jpg')
#         with open(file=FilePath, mode='rb') as f:
#             return HttpResponse(content=f, content_type='image/png')
#
#     def post(self, request):
#         return HttpResponse('这是 POST')
#

# 图片 视频版
# def image(request):
#     if request.method == "GET":
#         md5 = request.GET.get('md5')
#         print('----------------->md5',md5)
#         imgfile = os.path.join(IMAGES_DIR, md5 + '.jpg')
#         # print(imgfile)
#         if not os.path.exists(imgfile):
#             return Http404()
#         else:
#             data = open(imgfile, 'rb').read()
#             # return HttpResponse(content=data, content_type='image/png')
#             return FileResponse(open(imgfile, 'rb'), content_type='image/png')


# def image_text(request):
#
#     if request.method == 'GET':
#         md5 = request.GET.get('md5')
#         imgfile = os.path.join(IMAGES_DIR, md5 + '.jpg')
#         if not os.path.exists(imgfile):
#             return utils.response.wrap_json_response(
#                 code=utils.response.ReturnCode.RESOURCES_NOT_FOUND)
#         else:
#             response_data = {}
#             response_data['name'] = md5 + '.jpg'
#             # response_data['url'] = '/api/v1.0/service/images?md5=%s' % (md5)
#             response_data['url'] = '/service/images?md5=%s' % (md5)
#             response = utils.response.wrap_json_response(data=response_data)
#             return JsonResponse(data=response, safe=False)


# 视频版 类视图
class ImageViews(View, utils.response.CommonRequestMixin):
    def get(self, request):
        md5 = request.GET.get('md5')
        imgfile = os.path.join(IMAGES_DIR, md5)
        print(imgfile)
        if os.path.exists(imgfile):
            print('---------------------------->', os.path.exists(imgfile))
            return HttpResponse(open(imgfile, 'rb'), content_type='image/png')
        else:
            print('<-----------', os.path.exists(imgfile))
            response = self.wrap_json_response(code=utils.response.ReturnCode.RESOURCES_NOT_FOUND)
            return JsonResponse(data=response, safe=False)

    def post(self, request):
        # 获取文件 返回 key(文件名),value(文件内容)对象
        files = request.FILES
        response = []
        for key, value in files.items():
            content = value.read()
            md5 = hashlib.md5(content).hexdigest()
            path = os.path.join(IMAGES_DIR, md5 + '.jpg')
            with open(path, 'wb') as f:
                f.write(content)
            response.append({
                'name': key,
                'md5': md5
            })
        message = 'post message success'
        # response = utils.response.wrap_json_response(message=message)
        response = self.wrap_json_response(data=response,
                                           code=utils.response.ReturnCode.SUCCESS,
                                           message=message)
        return JsonResponse(data=response, safe=False)

    def delete(self, request):
        # 取出文件名字
        img_name = request.GET.get('md5')
        # print('===============>'+img_name)
        # 判断这个名字存不存在
        # img_name = md5 + '.jpg'
        # 文件路径
        path = os.path.join(IMAGES_DIR, img_name)
        # print('<<<========='+path)
        if os.path.exists(path):
            os.remove(path)
            message = 'remove success.'
        else:
            message = 'file(%s) not found.' % img_name
            # response = utils.response.wrap_json_response(message=message)
        response = self.wrap_json_response(code=utils.response.ReturnCode.SUCCESS,
                                           message=message)
        return JsonResponse(data=response, safe=False)

    # def put(self, request):
    #     message = 'put message success'
    #     # response = utils.response.wrap_json_response(message=message)
    #     response = self.wrap_json_response(message=message)
    #     return JsonResponse(data=response, safe=False)
