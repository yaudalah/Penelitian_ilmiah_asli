from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.core.paginator import Paginator

def HomeView(request):
    p = Paginator(Post.objects.all(), 3)
    page = request.GET.get('page')
    posts = p.get_page(page)

    return render(request, 'home/index.html',{'posts': posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'home/article_details.html'
    
class About(ListView):
    model = Post