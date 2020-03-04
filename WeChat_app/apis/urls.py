from django.urls import path, include
from .views import weather, menu, images,\
    session_cookie,Login,authorize,Logout

urlpatterns = [
    # path('', weather.helloworld),
    # path('', weather.weather),
    # path('weather', weather.weather),
    path('weather', Logout.Weather.as_view()),
    path('menu', menu.get_menu),
    # path('images/', images.get_image),
    # path('images/', images.ImageView.as_view()),
    # 图片  视频版
    # path('images', images.image),
    # 图文
    # path('imagetext', images.image_text),
    # 类视图
    path('imageview', images.ImageViews.as_view()),
    path('session', session_cookie.Session.as_view()),
    path('cookie', session_cookie.Cookie.as_view()),
    # 用户验证
    path('authorizelogin', Login.Authorize.as_view()),
    # 添加用户的关注的东西
    path('authorize', authorize.UserView.as_view()),
    # 注销用户登录
    path('logout', Logout.Logout.as_view()),
    # 判断用户状态
    path('status', Logout.Status.as_view()),
]
