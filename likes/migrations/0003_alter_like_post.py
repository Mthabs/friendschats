# Generated by Django 3.2.23 on 2023-12-14 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_likes'),
        ('likes', '0002_alter_like_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='posts.post'),
        ),
    ]