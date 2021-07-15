from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'home/index.html'
    ordering = ['-date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'home/article_details.html'
    # paginate_by = 5
    # queryset = Post.objects.order_by('-date')

class About(ListView):
    model = Post
    template_name = 'home/about-me.html'