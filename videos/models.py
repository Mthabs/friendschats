from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like
from comments.models import Comment

class Video(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = GenericRelation(Like, related_query_name='video_likes')
    comments = GenericRelation(Comment, related_query_name='video_comments')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Video by {self.owner.username}: {self.title}"
