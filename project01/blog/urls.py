"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='published-list'),
    path('draft/', views.DraftListView.as_view(), name='draft-list'),
    path('post/create/', views.PostCreateView.as_view(), name='post-new'),
    path('post/<slug:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<slug:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:pk>/publish/', views.publish_post, name='post-publish'),
    path('comment/<slug:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('comment/<slug:pk>/publish/', views.approve_post, name='approve-post'),
]
