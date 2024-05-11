from django.urls import path
from .views import PrayerTimingsAPIView

urlpatterns = [
    path('prayer-timings/<str:date>/<str:city_name>/<str:country_name>/', PrayerTimingsAPIView.as_view(), name='prayer_timings'),
]
