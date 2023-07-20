from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
# from django.db.models import Q

# Create your views here.

### Index
# class Index(View):
#     def get(self, request):
#         pass
#     def post(self, request):
#         pass


### Post
class PostListView(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        context = {
            'posts' : posts
        }

        return render(request, 'blog/post_list.html', context)


class PostCreateView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class PostDetailView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass



class PostUpdateView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


class PostDeleteView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass



class PostSearchView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


### Comment
class CommentCreateView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass



class CommentUpdateView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass



class CommentDeleteView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass



### ReComment
class ReCommentCreateView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass



class ReCommentUpdateView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass



class ReCommentDeleteView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


