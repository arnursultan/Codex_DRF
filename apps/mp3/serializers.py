# Импорты
from rest_framework import serializers
from .models import Mail


# Определяем сериализатор MailSerializer на основе модели Mail
class MailSerializer(serializers.ModelSerializer):
    class Meta:
        # Указываем модель, которая будет использоваться для сериализации и десериализации данных
        model = Mail

        # Указываем список полей, которые должны быть включены в сериализацию и десериализацию
        fields = ('id', 'video_url', 'email',)
