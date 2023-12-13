from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    image_filter_choices = [
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

    header = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'