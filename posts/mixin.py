from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Category

class MyMixinView(View):
    template =None
    model_name = None
    def get(self,request,post_id):
        post = self.model_name.objects.get(id=post_id)
        categories = Category.objects.all()
        data = {"post":post,"categories":categories}
        post.views += 1
        post.save()
        return render(request,self.template,data)