from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Photo
from .serializers import PhotoSerializer
from .permissions import IsOwnerOrReadOnly

class PhotoListCreateView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.userprofile)
        
class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsOwnerOrReadOnly]