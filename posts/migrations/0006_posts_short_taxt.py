# Generated by Django 4.1 on 2022-08-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_posts_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='short_taxt',
            field=models.CharField(default=1, max_length=100, verbose_name='Qisqa matn'),
            preserve_default=False,
        ),
    ]
