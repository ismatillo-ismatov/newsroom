# Generated by Django 4.1 on 2022-08-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_posts_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
