from rest_framework import serializers
from .models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user.username')
    profile_picture = serializers.ReadOnlyField(source='user.userprofile.profile_picture_url')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Photo
        fields = ['id', 'owner', 'profile_picture', 'image', 'caption', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        default_profile_picture_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_yansvo.jpg'

        if 'profile_picture' not in representation:
            representation['profile_picture'] = default_profile_picture_url
            
        return representation

    def validate_image(self, value):
        if value:
            max_size = 2 * 1024 * 1024  # 2 MB
            if value.size > max_size:
                raise serializers.ValidationError('Image size cannot exceed 2 MB.')
            if value.height > 4096:
                raise serializers.ValidationError('Image height cannot exceed 4096px.')
            if value.width > 4096:
                raise serializers.ValidationError('Image width cannot exceed 4096px.')
        return value