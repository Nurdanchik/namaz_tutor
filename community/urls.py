from django.urls import path
from .views import CommunityInfoAPIView, CommunitiesAPIView, CommunityCommentsAPIView, CreateCommunityAPIView, CreateCommentAPIView

urlpatterns = [
    path('communities/', CommunitiesAPIView.as_view(), name='community_list'),
    path('communities/<int:community_id>/info', CommunitiesAPIView.as_view(), name='community_info'),
    path('communities/<int:community_id>/comments', CommunityCommentsAPIView.as_view(), name='community_comments'),
    path('communities/create/', CreateCommunityAPIView.as_view(), name='create_community'),
    path('communities/<int:community_id>/comments/create/', CreateCommentAPIView.as_view(), name='create_comment'),
]