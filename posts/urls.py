from django.urls import path
from .views import *



app_name = 'posts'

urlpatterns = [
    path('base',BaseTemplateView.as_view(),name='base'),
    path('',IndexListView.as_view(),name='index'),
    path('tags/<int:tag_id>/',Tag_view.as_view(),name="tag_view"),
    # path('category/<int:pk>',CategoryView.as_view(),name='category'),
    # path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('category/<int:category_id>/posts',CategoryView.as_view(),name="category"),
    path('post/<int:post_id>/',MixinPost.as_view(),name="post-detail"),
    path('audio',AudioListView.as_view(),name='audio'),
    # path('search/',search_results,name="search"),
    path('search',search_post,name='search_post'),
    path('contact',contact,name='contact'),
    path('about',AboutView.as_view(),name='about'),
    path('exem',exemple,name='exem')
]