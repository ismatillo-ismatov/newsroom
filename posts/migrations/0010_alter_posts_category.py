# Generated by Django 4.1 on 2022-09-03 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postlar', to='posts.category'),
        ),
    ]
