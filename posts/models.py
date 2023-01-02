from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from embed_video.fields import EmbedVideoField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image', blank=True)
    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField('Tag nomi',max_length=50)

    def __str__(self):
        return self.title



class Posts(models.Model):
    category = models.ForeignKey(Category,related_name='postlar',on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Muolif')
    title = models.CharField(max_length=100)
    image = models.ImageField('image',upload_to='image',blank=True)
    audio = models.FileField('audi',upload_to='music',blank=True)
    views = models.PositiveIntegerField(default=0)
    tag = models.ManyToManyField(Tag,related_name='posts',blank=True)
    quote = models.CharField(max_length=200,verbose_name="Qisqa matn",blank=True)
    text = RichTextUploadingField(verbose_name="Xabar")
    video = EmbedVideoField(blank=True)
    post_date = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField('ism',max_length=30)
    image = models.ImageField(upload_to='team_image')
    professional = models.CharField(max_length=50)
    about = models.TextField()
