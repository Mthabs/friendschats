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
        image = self.request.data.get('image', None)
        if not image:
            default_image_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_yansvo.jpg'
            serializer.validated_data['image'] = default_image_url
        else:
            try:
                result = uploader.upload(image)
                serializer.validated_data['image'] = result['secure_url']
            except uploader.Error as e:
                print(f"Cloudinary Error: {e}")
                raise serializers.ValidationError({'image': [str(e)]})

        serializer.save(owner=self.request.user)

class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    

class PhotoLikeView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.likes.add(request.user.userprofile.like)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class PhotoUnlikeView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.likes.remove(request.user.userprofile.like)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)