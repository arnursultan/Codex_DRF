# Импорты
from rest_framework.routers import DefaultRouter
from .views import MailViewSet

# Создаем экземпляр DefaultRouter
router = DefaultRouter()

# Регистрируем MailViewSet в роутере с указанием URL-префикса 'mail' и базового имени 'mail'
router.register(r'mail', MailViewSet, basename='mail')

# urlpatterns - это список URL-маршрутов
urlpatterns = router.urls