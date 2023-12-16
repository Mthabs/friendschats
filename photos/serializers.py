from rest_framework import serializers
from .models import Photo
from .models import Likephoto
from PIL import Image


class PhotoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user.username')
    is_owner = serializers.SerializerMethodField()
    likephoto_id = serializers.SerializerMethodField()
    

    class Meta:
        model = Photo
        fields = ['id', 'owner', 'image', 'caption', 'created_at', 'updated_at', 'likephoto_id','is_owner']
        

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        default_image_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_yansvo.jpg'

        if 'image' not in representation:
            representation['image'] = default_image_url

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

    def get_likephoto_id(self, obj):
        user = self.context['request'].user
        try:
            likephoto_instance = Likephoto.objects.get(owner=user, photo=obj)
            return likephoto_instance.id
        except Likephoto.DoesNotExist:
            return None