from django.urls import path
from .views import *

urlpatterns = [
    path('',blog_post_list),
    path('<slug>',blog_post_detail),
    path('<slug>/edit',blog_post_update),
    path('<slug>/delete',blog_post_delete),
]