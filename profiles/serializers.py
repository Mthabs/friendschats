from rest_framework import serializers
from .models import UserProfile
from followers.models import Follower

class UserProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['id', 'owner', 'created_at', 'updated_at', 'bio', 'content', 'profile_picture', 'cover_photo','following_id', 'is_owner']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        default_profile_picture_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_yansvo.jpg'
        default_cover_photo_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_ifketo.jpg'
            
        if not instance.profile_picture:
            representation['profile_picture'] = default_profile_picture_url

        if not instance.cover_photo:
            representation['cover_photo'] = default_cover_photo_url

        return representation

    
    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        try:
            following = Follower.objects.get(owner=user, followed=obj.owner)
            return following.id
        except Follower.DoesNotExist:
            return None