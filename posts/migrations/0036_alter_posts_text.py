# Generated by Django 4.1.3 on 2022-11-20 00:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0035_alter_posts_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Xabar'),
        ),
    ]
