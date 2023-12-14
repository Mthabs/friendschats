from django.urls import path
from .views import (
    VideoListCreateView,
    VideoDetailView,
    VideoLikeView,
    VideoUnlikeView,
    VideoCommentCreateView,
)

urlpatterns = [
    path('videos/', VideoListCreateView.as_view(), name='video-list-create'),
    path('videos/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('videos/<int:pk>/like/', VideoLikeView.as_view(), name='video-like'),
    path('videos/<int:pk>/unlike/', VideoUnlikeView.as_view(), name='video-unlike'),
    path('videos/<int:pk>/comments/', VideoCommentCreateView.as_view(), name='video-comment-create'),
]