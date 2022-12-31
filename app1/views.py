from django.shortcuts import render
from app1.forms import ContactForm, NewsletterForm
def index(req):
    return render(req, 'website/index.html')

def about(req):
    return render(req, 'website/about.html')

def contact(req):
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(req, 'website/contact.html', {'form':form})


def newsletter_view(req):
    if req.method == 'POST':
        form = NewsletterForm(req.POST)
        if form.is_valid():
            form.save()
            Http
    else:
        return Http

