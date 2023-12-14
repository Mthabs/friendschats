from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from .models import Photo
from .serializers import PhotoSerializer
import cloudinary
from cloudinary import uploader

class PhotoListCreateView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        image = self.request.data.get('image', None)
        if not image:
            default_image_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_yansvo.jpg'
            serializer.validated_data['image'] = default_image_url
        else:
            try:
                # Attempt to upload the image to Cloudinary
                result = uploader.upload(image)
                # Extract the URL of the uploaded image from the Cloudinary response
                serializer.validated_data['image'] = result['secure_url']
            except uploader.Error as e:
                # Print the error message for debugging
                print(f"Cloudinary Error: {e}")
                raise serializers.ValidationError({'image': [str(e)]})

        # Use self.request.user (a User instance) as the owner
        serializer.save(owner=self.request.user.userprofile)

class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PhotoLikeView(generics.UpdateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.likes.add(request.user.userprofile.like)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class PhotoUnlikeView(generics.UpdateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.likes.remove(request.user.userprofile.like)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)