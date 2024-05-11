from rest_framework import generics, permissions
from .serializers import CommunitySerializer, CommentSerializer
from .models import Community, Comment
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class CommunitiesAPIView(generics.ListAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticated]

class CommunityInfoAPIView(generics.ListAPIView):
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        community_id = self.kwargs['community_id']
        return Community.objects.filter(id=community_id)

class CommunityCommentsAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        community_id = self.kwargs['community_id']
        return Comment.objects.filter(community=community_id)


class CreateCommunityAPIView(APIView):
    def post(self, request):
        # Получаем текущего пользователя из запроса
        author = request.user

        # Копируем данные запроса, чтобы их можно было изменить
        mutable_data = request.data.copy()

        # Добавляем автора в данные запроса
        mutable_data['author'] = author.id

        serializer = CommunitySerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateCommentAPIView(APIView):
    def post(self, request, community_id):
        # Получаем текущего пользователя из запроса
        user = request.user

        # Подставляем коммьюнити из URL
        community = Community.objects.get(pk=community_id)

        # Копируем данные запроса, чтобы их можно было изменить
        mutable_data = request.data.copy()

        # Добавляем пользователя и коммьюнити в данные запроса
        mutable_data['user'] = user.id
        mutable_data['community'] = community.id

        serializer = CommentSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)