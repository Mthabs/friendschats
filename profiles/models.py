from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.dispatch import receiver

class UserProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='image/', null=True, blank=True)
    cover_photo = models.ImageField(upload_to='image/', null=True, blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

#@receiver(post_save, sender=User)
#def create_profile(sender, instance, created, **kwargs):
#    if created:
#        UserProfile.objects.create(owner=instance)

#@receiver(post_save, sender=User)
#def save_profile(sender, instance, **kwargs):
#    instance.userprofile.save()
