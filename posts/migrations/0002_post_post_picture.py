# Generated by Django 3.2.23 on 2023-12-13 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_picture',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]
