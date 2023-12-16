from django.db import models
from django.contrib.auth.models import User
from likevideos.models import Likevideo


class Video(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Video by {self.owner.username}: {self.title}"

    @property
    def comment_count(self):
        return self.videocomments.count()