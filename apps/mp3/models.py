# Импорты
from django.db import models


#Создаем класс
class Mail(models.Model):
    # URL видео, которое пользователь хочет конвертировать
    video_url = models.URLField(max_length=200)

    # Адрес электронной почты пользователя, на который будет отправлено письмо
    email = models.EmailField()

    def __str__(self):
        # Возвращаем строку для отображения в административной панели
        return f"Conversion Request ({self.id}) - Email: {self.email}"
