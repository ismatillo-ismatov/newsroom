from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate,gettext
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic.list import MultipleObjectMixin
from django.core import paginator
from .models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .mixin import MyMixinView
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import Response
from django.http import HttpResponse,HttpResponseRedirect
from .serializers import *
import datetime
import json
from django.http import JsonResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail,BadHeaderError
from .form import ContactForm
from  django.urls import reverse_lazy
class BaseTemplateView(generic.TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        today = datetime.datetime.now().strftime("%I: %M %P on %B %d %y")
        context = super(BaseTemplateView, self).get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context['tags']= Tag.objects.all()
        context['trans']= translate(language='uz')

        return context

class IndexListView(generic.ListView):
    model = Category
    context_object_name = "categories"
    template_name = 'index.html'



    def get_queryset(self):

        return Category.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(IndexListView, self).get_context_data(*args,**kwargs)
        context["categories"] = Category.objects.all()
        context['posts'] = Posts.objects.all()
        context['post2'] = Posts.objects.all().order_by('post_date')
        context['tags'] = Tag.objects.all()
        trans = translate(language='uz')
        context['trans']= trans
        return context

class CategoryView(generic.View):
    def get(self,request,category_id):
        categories = Category.objects.all()
        tags = Tag.objects.all()
        try:
            category = Category.objects.get(id=category_id)
        except:
            return render(request,'404.html')
        posts = category.postlar.all()
        paginator = Paginator(posts,20,orphans=0,allow_empty_first_page=True)
        if "page" in request.GET:
            page_num = request.GET['page']
        else:
            page_num = 1
        page = paginator.get_page(page_num)
        context = {'post':page.object_list,"page":page,'category':category,'categories':categories,'tags':tags}
        return render(request,"category.html",context)






class PostDetailView(generic.DetailView):
    template_name = 'single.html'
    model = Posts
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['posts']=Posts.objects.filter(tags__in=self.object.posts.all())
        context['tag']=Tag.objects.all()
        trans = translate(language='uz')
        context['trans']= trans
        return context



class MixinPost(MyMixinView):
    template = "single.html"
    model_name = Posts




class AudioListView(generic.View):
    def get(self,request):
        categories = Category.objects.all()
        posts = Posts.objects.all()
        paginator = Paginator(posts,5, orphans=0, allow_empty_first_page=True)
        if "page" in request.GET:
            page_num = request.GET['page']
        else:
            page_num = 1
        page = paginator.get_page(page_num)
        context = {'posts':page.object_list,'page':page,'categories':categories}
        return render(request,"audio.html",context)





class Tag_view(generic.View):
    def get(self,request,tag_id):
        try:
            tag = Tag.objects.get(id=tag_id)
        except:
            return render(request,'404.html',)
        post = tag.posts.all()
        category = Category.objects.all()
        c = {'posts':post,'tag':tag,"category":category}
        return render(request,'tags.html',c)

@api_view(('GET',))
def search_post(request):
    value = request.GET.get("data")
    posts = Posts.objects.filter(title__icontains=value)
    serial = PostSeliazator(posts,many=True)
    data = {"posts":posts}
    return Response(serial.data)







def exemple(request):
    if 'term' in request.GET:
        qs = Posts.objects.filter(title__icontains=request.GET.get('term'))
        titles = list()
        for posts in qs:
            titles.append(posts.title)
        return JsonResponse(titles,safe=False)
    return render(request,'exemple.html')

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text



# class ContactView(generic.FormView):
#     template_name = 'contact.html'
#     form_class = ContactForm
#     success_url = reverse_lazy('contact:success')
    # def get_context_data(self, **kwargs):
        # categories = Category.objects.all()


    # def form_valid(self, form):
    #     form.send()
    #     return super().form_valid(form)


def contact(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            html = render_to_string('contactform.html',{'name':name,'email':email,'message':message})

            send_mail(
                'llo there',
                'text test',
                'ismatilloismatov1995@gmail.com',
                ['ismatilloismatov1995@gmail.com'],
                html_message=html
        )
            return redirect('contact')

    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form,'categories':categories})






class AboutView(generic.TemplateView):
    template_name = 'abaut.html'
    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        team = Team.objects.all()
        context = {"team":team,'categories':categories}
        return context






# @login_required()
# def search_results(request):
#     if request.is_ajax():
#         posts = request.POST.get('posts')
#         qs = Posts.objects.filter(name__icontaions=posts)
#         qs
#         print(posts)
#         return JsonResponse({'data': posts})
#     return JsonResponse({})


