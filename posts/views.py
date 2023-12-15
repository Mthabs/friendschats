from rest_framework import generics, permissions
from friends_chats.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer

class PostListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    