from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from likes.models import Like
from likes.serializers import LikeSerializer
from comments.models import Comment
from comments.serializers import CommentSerializer

class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VideoLikeView(generics.UpdateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        video_instance = self.get_object()
        like, created = Like.objects.get_or_create(owner=request.user, content_type=video_instance, object_id=video_instance.id)
        serializer = LikeSerializer(like)
        return Response(serializer.data)

class VideoUnlikeView(generics.UpdateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        video_instance = self.get_object()
        Like.objects.filter(owner=request.user, content_type=video_instance, object_id=video_instance.id).delete()
        return Response(status=204)