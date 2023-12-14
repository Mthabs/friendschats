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

class PhotoLikeView(generics.UpdateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.likes.add(request.user.userprofile)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)