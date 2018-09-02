from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

class About(TemplateView):
    template_name = "blog/about.html"

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    success_url = reverse_lazy('post-list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    template_name = 'blog/draft.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=timezone.now()).order_by('-create_date')

########################################################################################################################

@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk)
    post.publish
    return redirect("post-detail", pk=pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {
        "form" : form
    })

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk)
    comment.approve()
    return redirect("post-detail", pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk):
    post_pk = comment.post.pk
    comment.delete()
    return redirect("post-detail", pk=post_pk)
