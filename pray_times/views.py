from rest_framework import generics
from rest_framework.response import Response
from requests import get


class PrayerTimingsAPIView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        date = kwargs.get('date')
        city_name = kwargs.get('city_name')
        country_name = kwargs.get('country_name')

        # Формируем URL для запроса к API Aladhan
        api_url = f'http://api.aladhan.com/v1/timingsByCity/{date}?city={city_name}&country={country_name}'

        # Отправляем GET-запрос к API Aladhan
        response = get(api_url)

        # Проверяем успешность запроса
        if response.status_code == 200:
            # Возвращаем JSON-ответ от API Aladhan
            return Response(response.json())
        else:
            # Если запрос не удался, возвращаем соответствующее сообщение об ошибке
            return Response({'error': 'Failed to fetch prayer timings'}, status=response.status_code)