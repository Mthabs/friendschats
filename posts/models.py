from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like
from comments.models import Comment

class Post(models.Model):
    IMAGE_FILTER_CHOICES = [
        ('normal', 'Normal'),
        ('black_and_white', 'Black and White'),
        ('sepia', 'Sepia'),
        ('vintage', 'Vintage'),
        ('grayscale', 'Grayscale'),
        ('warm', 'Warm Tone'),
        ('cool', 'Cool Tone'),
        ('invert', 'Invert Colors'),
        ('blur', 'Blur'),
        ('sharpen', 'Sharpen'),
    ]
    header = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    post_picture = models.ImageField(upload_to='post_images/', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = GenericRelation(Like, related_query_name='post_likes')
    comments = GenericRelation(Comment, related_query_name='post_comments')
    image_filter = models.CharField(
        max_length=32,
        choices=IMAGE_FILTER_CHOICES,
        default='normal',
        blank=True,
        null=True
    )
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_at']

    def __str__(self):
        return f"Post by {self.id} at {self.header}"