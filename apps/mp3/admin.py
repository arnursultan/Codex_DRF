# Импорты
from django.contrib import admin
from .models import Mail

# Регистрируем модель Mail в административной панели
@admin.register(Mail)
# Создаем класс администратора для модели Mail
class MailAdmin(admin.ModelAdmin):
    pass
