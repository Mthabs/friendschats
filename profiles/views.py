from rest_framework import generics, permissions, serializers
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
   


