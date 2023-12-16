from rest_framework import serializers
from .models import Videocomment


class VideocommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='user.userprofile.id')
    profile_picture = serializers.ReadOnlyField(source='user.userprofile.profile_picture_url')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Videocomment
        fields = ['id', 'profile_id', 'owner', 'video', 'content', 'created_at', 'updated_at', 'profile_picture', 'is_owner']

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner

class VideocommentDetailSerializer(VideocommentSerializer):
    video = serializers.ReadOnlyField(source='video.id')
