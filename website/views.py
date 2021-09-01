from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.core.paginator import Paginator
from django.http import Http404

def HomeView(request):
    context = {}

    try:
        context["paginator"] = Paginator(Post.objects.all(), 3)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    context["page"] = request.GET.get('page')
    context["posts"] = context["paginator"].get_page(context["page"])
    context["page_nums"] = "a" *  context["posts"].paginator.num_pages

    return render(request, 'home/index.html', context)

def ArticleDetailView(request, post_id):
    context={}

    try:
        context["current_post"] = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    return render(request, 'home/article_details.html', context)
    
class About(ListView):
    model = Post