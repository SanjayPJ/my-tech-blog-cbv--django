from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm

# Create your views here.

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
class DraftListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=timezone.now()).order_by('-created_date')
    
class PostDetailView(DetailView,):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('published-list')

class PostCreateView(CreateView):
    model = Post
    fields = ["user", "title", "body",]

class PostUpdateView(UpdateView):
    model = Post
    fields = ["user", "title", "body",]

def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post-detail', pk=pk)
    
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('published-list')

def approve_post(request, pk):
    post = get_object_or_404(Comment, pk=pk)
    post.approve_comment()
    return redirect('published-list')