# Generated by Django 4.1 on 2022-10-10 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_posts_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='video',
            field=models.FileField(default=0, upload_to='video', verbose_name='video'),
            preserve_default=False,
        ),
    ]