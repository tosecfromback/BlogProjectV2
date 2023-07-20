from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy, reverse

# Create your views here.

### Index
# class Index(View):
#     def get(self, request):
#         pass
#     def post(self, request):
#         pass


### Post
class PostList(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        context = {
            'posts' : posts,
            'title' : "BlogPostsPage"
        }

        return render(request, 'blog/post_list.html', context)


class PostCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        context = {
            'form' : form,
            'title' : "Blog"
        }

        return render(request, 'blog/post_form.html', context)
    
    def post(self, request):
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('blog:list')
        
        context = {
            'form' : form
        }

        return render(request, 'blog/post_form.html', context)


class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.prefetch_related('comment_set').get(pk=pk)

        comments = post.comment_set.all()

        comment_form = CommentForm

        context = {
            "title" : "BlogPost",
            'post_id' : pk,
            'post_title' : post.title,
            'post_writer' : post.writer,
            'post_content' : post.content,
            'post_updated_at' : post.updated_at,
            'comments' : comments,
            'comment_form' : comment_form,
        }

        return render(request, 'blog/post_detail.html', context)


class PostUpdate(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(initial={'title':post.title, 'content': post.content})
        context = {
            'form' : form,
            'post' : post,
            "title" : "BlogEdit",
        }

        return render(request, 'blog/post_eidt.html', context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST)

        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', pk=pk)
        
        context = {
            'form' : form,
            "title" : "BlogPost"
        }

        return render(request, 'blog/post_edit.html', context)


class PostDelete(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.visible = False
        post.save()
        return redirect('blog:list')


class PostSearch(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


### Comment
class CommentCreate(LoginRequiredMixin, View):
    
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=pk)

        if form.is_valid():
            content = form.cleaned_data['content']
            writer = request.user

            try:
                comment = Comment.objects.create(post=post, content=content, writer=writer)
            except ObjectDoesNotExist as e:
                print('Post does not exist.', str(e))
            except ValidationError as e:
                print('Valdation error occurred', str(e))
            
            return redirect('blog:detail', pk=pk)
        
        context = {
            "title": "Blog",
            'post_id': pk,
            'comments': post.comment_set.all(),
            'hashtags': post.hashtag_set.all(),
            'comment_form': form
        }
        return render(request, 'blog/post_detail.html', context)



class CommentUpdate(View):
    def get(self, request):
        pass
    def post(self, request):
        pass



class CommentDelete(View):
    def post(self, request, pk):
        Comment = get_object_or_404(Comment, pk=pk)
        Comment.visible = False
        Comment.save()
        return redirect('blog:list')



# ### ReComment
# class ReCommentCreate(View):
#     def get(self, request):
#         pass
#     def post(self, request):
#         pass



# class ReCommentUpdate(View):
#     def get(self, request):
#         pass
#     def post(self, request):
#         pass



# class ReCommentDelete(View):
#     def get(self, request):
#         pass
#     def post(self, request):
#         pass


