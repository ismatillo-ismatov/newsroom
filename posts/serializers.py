from rest_framework import serializers
from .models import *

class PostSeliazator(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ("id","title","image")