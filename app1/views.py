from django.shortcuts import render

def index(req):
    return render(req, 'website/index.html')

def about(req):
    return render(req, 'website/about.html')

def contact(req):
    return render(req, 'website/contact.html')