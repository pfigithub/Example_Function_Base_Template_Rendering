from blog.views import *
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name = 'index_blog'),
    path('<int:pid>', blog_single, name = 'single_blog')
]