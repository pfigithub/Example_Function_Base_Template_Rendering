from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_view(req):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(req, 'blog/blog-home.html', context)


def blog_single(req, pid):
    post = get_object_or_404(Post, pk=pid, status =1)
    context = {'post': post}
    return render(req, 'blog/blog-single.html', context)
