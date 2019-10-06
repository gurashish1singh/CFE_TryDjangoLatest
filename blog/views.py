from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import *

# Create your views here.

########### OLD VIEWS 

# # View all the posts
# def blog_post_list(request):

#     post_list = BlogPost.objects.all()
#     template_name = 'blog_post_list.html'
#     context = {
#         'title' : 'List',
#         'post' : post_list,
#     }
#     return render(request,template_name,context)

# # View the details of a post
# def blog_post_detail(request,slug):

#     # If slugs are not unique
#     # obj = BlogPost.objects.filter(slug=slug) # query>databse>data>django renders
#     # if obj.count() >= 1:
#     #     obj = obj.first()
#     # else:
#     #     raise Http404
    
#     obj = get_object_or_404(BlogPost, slug=slug)
#     template_name = 'blog_post_detail.html'
#     context = {
#         'title' : obj.title,
#         'object' : obj,
#     }
#     return render(request,template_name,context)

################ NEW CRUD VIEWS ##############
# List View
def blog_post_list(request):

    post_list = BlogPost.objects.all()
    template_name = 'blog/list.html'
    context = {
        'title' : 'List of all Posts',
        'object_list' : post_list,
    }
    return render(request,template_name,context)

# Create view
def blog_post_create(request):

    
    template_name = 'blog/create.html'
    context = {
        'title' : 'Create a Post',
        'form' : None,
    }
    return render(request,template_name,context)

# Retrive View
def blog_post_detail(request, slug):

    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {
        'title' : obj.title,
        'object' : obj,
    }
    return render(request,template_name,context)

# Update view
def blog_post_update(request, slug):

    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = {
        'title' : obj.title,
        'object' : obj,
        'form' : None,
    }
    return render(request,template_name,context)

# Delete View
def blog_post_delete(request, slug):

    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {
        'title' : obj.title,
        'object' : obj,
        'form' : None,
    }
    return render(request,template_name,context)