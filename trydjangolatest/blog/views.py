from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import *

from .forms import *

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

    post_list = BlogPost.objects.all().published # To view only the blogs that have been published!
    if request.user.is_authenticated:
        post_list = BlogPost.objects.filter(user=request.user)
        # post_list = (post_list | my_post_list).distinct()
    template_name = 'blog/list.html'
    context = {
        'title' : 'List of all Posts',
        'object_list' : post_list,
    }
    return render(request,template_name,context)

# Login required validation
@login_required(login_url='/login')
# @staff_member_required
# Create view
def blog_post_create(request):

    form = BlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)    # Shows data on the terminal
        # obj = BlogPost.objects.create(**form.cleaned_data) # This saves the data in the database, if using forms.form
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        # form.save() # if using forms.ModelForm
        form = BlogPostForm()
    template_name = 'blog/form.html'
    context = {
        'title' : 'Create a Post',
        'form' : form,
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
# Login required validation
@login_required(login_url='/login')
# @staff_member_required
def blog_post_update(request, slug):

    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'blog/form.html'
    context = {
        'title' : f'Update {obj.title}',
        # 'object' : obj,
        'form' : form,
    }
    return render(request,template_name,context)

# Delete View
# Login required validation
@login_required(login_url='/login')
# @staff_member_required
def blog_post_delete(request, slug):

    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect ('/blog')
    context = {
        'title' : obj.title,
        'object' : obj,
        'form' : None,
    }
    return render(request,template_name,context)