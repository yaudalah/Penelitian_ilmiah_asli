from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'home/index.html'
    ordering = ['-date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'home/article_details.html'
    
class About(ListView):
    model = Post