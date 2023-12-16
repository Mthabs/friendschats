from rest_framework import serializers
from .models import Video
from .models import Likevideo

class VideoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    likevideo_id = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ['id', 'owner', 'title', 'video_file', 'description', 'created_at', 'updated_at', 'likevideo_id', 'is_owner']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        return representation


    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner

    def get_likevideo_id(self, obj):
        user = self.context['request'].user
        try:
            likevideo_instance = Likevideo.objects.get(owner=user, video=obj)
            return likevideo_instance.id
        except Likevideo.DoesNotExist:
            return None