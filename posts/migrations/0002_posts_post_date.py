# Generated by Django 4.1 on 2022-08-24 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='post_date',
            field=models.DateField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
