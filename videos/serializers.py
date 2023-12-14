from rest_framework import serializers
from .models import Video
from likes.serializers import LikeSerializer
from comments.serializers import CommentSerializer

class VideoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    likes = LikeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ['id', 'owner', 'title', 'video_file', 'description', 'created_at', 'updated_at', 'likes_count', 'comments_count', 'likes', 'comments']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes_count'] = instance.likes.count()
        representation['comments_count'] = instance.comments.count()
        
        return representation

    def get_likes_count(self, instance):
        return instance.likes.count()

    def get_comments_count(self, instance):
        return instance.comments.count()