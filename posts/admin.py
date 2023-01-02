from django.contrib import admin
from .models import *
from django import forms
from .translation import PostTranslation
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from embed_video.admin import AdminVideoMixin

admin.site.register(Tag)
class PostEditorform(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(),label='matn')

    class Meta:
        model = Posts
        fields = '__all__'

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id',"category","owner","title","post_date")
#
#     list_display_links = ('id','title')
#


@admin.register(Category)
class CategoryTranslateAdmin(TranslationAdmin):
    list_display = ('id','title')
    group_fieldsets = True

    class Media:
        js = (
                'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
                'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
                'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Posts)
class PostTranslateAdmin(TranslationAdmin):
    list_display = ("id","title",'image')
    list_display_links = ("id","title",'image')
    group_fieldsets = True

    class Media:
        js = (
                'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
                'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
                'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class MyModelAdmin(AdminVideoMixin,admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name',)