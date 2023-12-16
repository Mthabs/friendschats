from rest_framework import generics, permissions, serializers
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        user = self.request.user
        existing_profile = UserProfile.objects.filter(owner=user).first()

        # If a profile already exists, update it; otherwise, create a new one
        if existing_profile:
            serializer.update(existing_profile, serializer.validated_data)
        else:
            serializer.save(owner=user)

class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
   