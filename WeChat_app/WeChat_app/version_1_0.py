from django.urls import path, include

urlpatterns = [
    path('service/', include('apis.urls')),
    path('apps/', include('apis.urls')),
]
