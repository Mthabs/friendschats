# Generated by Django 3.2.23 on 2023-12-14 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes', '0002_alter_like_post'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_photos', to='likes.Like'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]