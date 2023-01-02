# Generated by Django 4.1 on 2022-10-13 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0026_remove_posts_video_alter_posts_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='url',
        ),
        migrations.AddField(
            model_name='posts',
            name='video',
            field=models.FileField(default=0, upload_to='video', verbose_name='video'),
            preserve_default=False,
        ),
    ]
