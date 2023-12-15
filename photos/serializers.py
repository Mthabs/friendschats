from rest_framework import serializers
from .models import Photo
from likes.serializers import LikeSerializer


class PhotoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user.username')
    profile_picture = serializers.ReadOnlyField(source='user.userprofile.profile_picture_url')
    is_owner = serializers.SerializerMethodField()

    likes_count = serializers.SerializerMethodField()
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Photo
        fields = ['id', 'owner', 'profile_picture', 'image', 'caption', 'created_at', 'updated_at', 'likes_count', 'likes','is_owner']
        

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes_count'] = instance.likes.count()
        default_profile_picture_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_yansvo.jpg'

        if 'profile_picture' not in representation:
            representation['profile_picture'] = default_profile_picture_url

        return representation

    def validate_image(self, value):
        if value:
            image = Image.open(value)
            max_size = 2 * 1024 * 1024  # 2 MB
            if value.size > max_size:
                raise serializers.ValidationError('Image size cannot exceed 2 MB.')
            max_height = 4096
            max_width = 4096
            if image.height > max_height or image.width > max_width:
                raise serializers.ValidationError('Image dimensions cannot exceed 4096x4096px.')

        return value
        
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_likes_count(self, instance):
        return instance.likes.count()