from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_view(req, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name= kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username= kwargs['author_username'])
    context = {'posts': posts}
    return render(req, 'blog/blog-home.html', context)


def blog_single(req, pid):
    post = get_object_or_404(Post, pk=pid, status =1)
    context = {'post': post}
    return render(req, 'blog/blog-single.html', context)


def blog_category(req, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(req, 'blog/blog-home.html', context)


def blog_search(req):
    posts = Post.objects.filter(status=1)
    if req.method == 'GET':
        if s:= req.GET.get('s'):
            posts = posts.filter(content__contains=s)

    context = {'posts': posts}
    return render(req, 'blog/blog-home.html', context)