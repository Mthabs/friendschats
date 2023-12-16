from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
#from django.db.models.signals import post_save
#from django.dispatch import receiver

class UserProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='image/', null=True, blank=True)
    cover_photo = models.ImageField(upload_to='image/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

    def get_posts_count(self):
        return self.posts.all().count()


#@receiver(post_save, sender=User)
#def create_profile(sender, instance, created, **kwargs):
#    if created:
#        UserProfile.objects.create(owner=instance)

#@receiver(post_save, sender=User)
#def save_profile(sender, instance, **kwargs):
#    instance.userprofile.save()
