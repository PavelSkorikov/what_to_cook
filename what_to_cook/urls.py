"""what_to_cook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # путь к админ - панели
    path('admin/', admin.site.urls),
    # все виды аутентификации
    path('auth/', include('djoser.urls')),
    path('auth_token/', include('djoser.urls.authtoken')),
    path('auth_jwt/', include('djoser.urls.jwt')),
    # путь к приложению main_app
    path('api/v1/main_app/', include('main_app.urls')),
    # подключаем базовую аутентификацию Django Rest (сессии)
    # path('api/v1/base-auth/', include('rest_framework.urls')),
]

# статические файлы будут раздаваться из дирректории MEDIA при включенном
# DEBUG - режиме.
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
