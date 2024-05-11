from django.urls import path
from .views import TutorialsAPIView, TutorialInfoAPIView

urlpatterns = [
    path('tutorials/', TutorialsAPIView.as_view(), name='tutorials'),
    path('tutorials/<int:tutorial_id>/info/', TutorialInfoAPIView.as_view(), name='tutorial_info'),
]