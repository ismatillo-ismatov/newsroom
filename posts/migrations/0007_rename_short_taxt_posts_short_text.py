# Generated by Django 4.1 on 2022-08-26 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_posts_short_taxt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='short_taxt',
            new_name='short_text',
        ),
    ]
