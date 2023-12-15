from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import Friend
from .serializers import FriendSerializer


class FriendListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FriendUnfriendView(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    
