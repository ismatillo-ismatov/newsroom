from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Posts)
class PostTranslation(TranslationOptions):
    fields = ('title','text')


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('title',)