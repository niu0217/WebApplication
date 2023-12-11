"""定义accounts的URL模式"""

from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    # 包含默认的身份认证URL
    path('', include('django.contrib.auth.urls')),
]
