from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import Photocomment
from .serializers import PhotocommentSerializer

class PhotocommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Photocomment.objects.all()
    serializer_class = PhotocommentSerializer
    
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PhotocommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Photocomment.objects.all()
    serializer_class = PhotocommentSerializer
