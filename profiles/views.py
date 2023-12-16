from django.db.models import Count
from rest_framework import generics, permissions, serializers
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        queryset = UserProfile.objects.annotate(
            posts_count=Count('owner__posts'),
            followers_count=Count('owner__following'),  
            following_count=Count('owner__followed')    
        )
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        existing_profile = UserProfile.objects.filter(owner=user).first()
        if existing_profile:
            serializer.update(existing_profile, serializer.validated_data)
        else:
            serializer.save(owner=user)

class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = UserProfileSerializer
    def get_queryset(self):
        queryset = UserProfile.objects.all()
        return queryset.annotate(posts_count=Count('owner__posts'))
   