# Generated by Django 4.1 on 2022-10-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0029_alter_posts_tag_alter_tag_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='posts', to='posts.tag'),
        ),
    ]
