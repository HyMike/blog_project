from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from .models import Post, Author, Tag
from django.views import View
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.urls import reverse
# Create your views here.


class IndexView(ListView):
    template_name = 'blog_app/index.html'
    model = Post
    ordering = ["-date"]
    context_object_name = 'latest_posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


def getPostDate(post):
    return post['date']


# def index(request):
#     filterDate = Post.objects.all().order_by('-date')

#     getLatestPost = filterDate[:3]
#     return render(request, "blog_app/index.html", {'latest_posts': getLatestPost})


class AllPostsView(ListView):
    template_name = 'blog_app/posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'


# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, "blog_app/posts.html", {'all_posts': all_posts})

class SpecificPostView(View):
    template_name = 'blog_app/specific_post.html'
    model = Post
    # context_object_name = 'specific_post'

    def readLater(self, request, post_id):
        stored_posts = request.session.get('stored_posts')

        if stored_posts is not None:
            postBoolean = post_id in stored_posts
        else:
            postBoolean = False

        return postBoolean

    def get(self, request, slug):
        correctPost = Post.objects.get(slug=slug)
        context = {
            'specific_post': correctPost,
            'tagCaption': correctPost.tag.all(),
            'comment_form': CommentForm(),
            'comments': correctPost.comments.all().order_by('id'),
            'postBoolean': self.readLater(request, correctPost.id)
        }
        return render(request, "blog_app/specific_post.html", context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        correctPost = Post.objects.get(slug=slug)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = correctPost
            comment.save()

            return HttpResponseRedirect(reverse('specific_post', args=[slug]))

        context = {
            'specific_post': correctPost,
            'tagCaption': correctPost.tag.all(),
            'comment_form': form,
            'comments': correctPost.comments.all().order_by('id'),
            'postBoolean': self.readLater(request, correctPost.id)


        }
        return render(request, "blog_app/specific_post.html", context)


# def specificPost(request, url_slug):
#     correctPost = Post.objects.get(slug=url_slug)
#     tagCaption = correctPost.tag.all()

#     return render(request, "blog_app/specific_post.html", {'specific_post': correctPost,
#                                                            'tagCaption': tagCaption})


# class CommentSection(View):
#     def post(self, request):
#         pass

class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = True
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = False

        return render(request, 'blog_app/stored_post.html', context)

    def post(self, request):
        stored_posts = request.session.get('stored_posts')

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session['stored_posts'] = stored_posts

        return HttpResponseRedirect('/')

        # read_later = request.POST['read_later']
