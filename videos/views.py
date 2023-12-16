from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer

class VideoListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
