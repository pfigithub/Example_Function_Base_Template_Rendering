from blog.views import *
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name = 'index_blog'),
    path('category/<str:cat_name>', blog_view, name = 'category'),
    path('<int:pid>', blog_single, name = 'single_blog')
]