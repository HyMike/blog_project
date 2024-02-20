from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "blog_app/index.html", {})


def posts(request):
    return render(request, "blog_app/posts.html", {})


def specific_post(request, slug):
    return render(request, "blog_app/specific_post.html", {"slug": slug})
