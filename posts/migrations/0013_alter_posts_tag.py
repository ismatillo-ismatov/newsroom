# Generated by Django 4.1 on 2022-09-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_tag_posts_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='posts', to='posts.tag'),
        ),
    ]
