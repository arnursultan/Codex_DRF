# Импорты
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.mp3.urls import router as MailViewSet

# Создаем экземпляр DefaultRouter
router = DefaultRouter()

# Расширяем реестр DefaultRouter с реестром из приложения 'apps.mp3.urls'
router.registry.extend(MailViewSet.registry)

# Определяем переменную urlpatterns - список URL-маршрутов приложения
urlpatterns = [
    # URL-маршрут для административной панели Django
    path('admin/', admin.site.urls),

    # URL-маршрут, который включает URL-маршруты из приложения 'apps.mp3.urls'
    path('', include('apps.mp3.urls'))
]
