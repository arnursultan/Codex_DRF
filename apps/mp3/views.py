# Импорты
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Mail
from .serializers import MailSerializer


# Создаем класс MailViewSet, который наследует от viewsets.ModelViewSet
class MailViewSet(viewsets.ModelViewSet):
    # Указываем queryset для получения всех объектов модели Mail
    queryset = Mail.objects.all()

    # Указываем сериализатор, который будет использоваться для сериализации и десериализации данных
    serializer_class = MailSerializer

    # Метод create обрабатывает создание новых объектов
    def create(self, request, *args, **kwargs):
        # Создаем экземпляр сериализатора на основе данных из запроса (request.data)
        serializer = self.get_serializer(data=request.data)

        # Проверяем валидность данных согласно правилам, определенным в сериализаторе
        serializer.is_valid(raise_exception=True)

        # Вызываем метод perform_create для сохранения объекта в базе данных
        self.perform_create(serializer)

        # Возвращаем успешный HTTP-ответ с данными созданного объекта и статусом 201 CREATED
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Метод destroy обрабатывает удаление объектов
    def destroy(self, request, *args, **kwargs):
        # Получаем объект, который нужно удалить
        instance = self.get_object()

        # Вызываем метод perform_destroy для удаления объекта из базы данных
        self.perform_destroy(instance)

        # Возвращаем успешный HTTP-ответ с пустым телом и статусом 204 NO CONTENT
        return Response(status=status.HTTP_204_NO_CONTENT)
