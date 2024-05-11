from rest_framework import generics, permissions
from . import models
from . import serializers

class TutorialsAPIView(generics.ListAPIView):
    queryset = models.Tutorial.objects.all()
    serializer_class = serializers.TutorialSerializer
    permission_classes = [permissions.IsAuthenticated]

class TutorialInfoAPIView(generics.ListAPIView):
    serializer_class = serializers.TutorialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tutorial_id = self.kwargs['tutorial_id']
        return models.Tutorial.objects.filter(id=tutorial_id)