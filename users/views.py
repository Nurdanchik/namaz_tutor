from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegistrationSerializer, LoginSerializer, UserInfoSerializer
from rest_framework import generics, permissions
from .models import CustomUser

class RegistrationAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer

class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer
    
class UserInfoAPIView(RetrieveAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        
        return CustomUser.objects.select_related().get(pk=self.request.user.pk)