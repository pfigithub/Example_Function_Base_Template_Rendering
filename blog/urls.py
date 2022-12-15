from blog.views import *
from django.urls import path

urlpatterns = [
    path('', blog_view, name = 'index_blog'),
    path('single', blog_single, name = 'single')
]