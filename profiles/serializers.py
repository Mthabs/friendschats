from rest_framework import serializers
from .models import UserProfile
from followers.models import Follower
from friends.models import Friend

class UserProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    friendship_id = serializers.SerializerMethodField()
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['id', 'owner', 'created_at', 'updated_at', 'name', 'content', 'profile_picture', 'cover_photo', 'following_id', 'friendship_id', 'is_owner', 'posts_count']

    def to_representation(self, instance):
        if isinstance(instance, UserProfile):
            representation = super().to_representation(instance)
            default_profile_picture_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_yansvo.jpg'
            default_cover_photo_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_ifketo.jpg'
                
            if not instance.profile_picture:
                representation['profile_picture'] = default_profile_picture_url

            if not instance.cover_photo:
                representation['cover_photo'] = default_cover_photo_url

            return representation
        return {}
        
    def get_is_owner(self, obj):
        if isinstance(obj, UserProfile):
            request = self.context.get('request')
            return request.user == obj.owner
        return False

    def get_posts_count(self, obj):
        return obj.owner.posts.all().count()

    def get_following_id(self, obj):
        if isinstance(obj, UserProfile):
            user = self.context['request'].user
            try:
                following = Follower.objects.get(owner=user, followed=obj.owner)
                return following.id
            except Follower.DoesNotExist:
                return None
        return None

    def get_friendship_id(self, obj):
        if isinstance(obj, UserProfile):
            user = self.context['request'].user
            try:
                friendship = Friend.objects.get(
                    owner=user, friend=obj.owner
                )
                return friendship.id
            except Friend.DoesNotExist:
                return None
        return None