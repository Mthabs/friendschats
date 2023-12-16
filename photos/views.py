from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .models import Photo
from .serializers import PhotoSerializer


class PhotoListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
