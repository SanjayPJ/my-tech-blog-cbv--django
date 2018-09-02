"""my_tech_blog URL Configuration

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
    path('', views.PostListView.as_view(), name='post-list'),
    path('about/', views.About.as_view(), name='about'),
    path('post/new/', views.PostCreateView.as_view(), name='post-new'),
    path('post/<slug:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:pk>/edit', views.PostUpdateView.as_view(), name='post-edit'),
    path('post/<slug:pk>/remove', views.PostDeleteView.as_view(), name='post-remove'),
    path('post/<slug:pk>/publish', views.publish_post, name='post-publish'),
    path('draft/', views.DraftListView.as_view(), name='post-draft-list'),
    path('post/<slug:pk>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<slug:pk>/approve', views.comment_approve, name='comment_approve'),
    path('comment/<slug:pk>/remove', views.comment_remove, name='comment_remove'),
    path('logout/', views.logout_view, name='logout_view'),
]
