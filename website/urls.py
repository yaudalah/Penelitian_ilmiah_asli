from django.urls import path
from .views import HomeView, ArticleDetailView, About
from django.conf.urls import url

urlpatterns = [
    path('', HomeView, name="home"),
    path('article/<int:post_id>', ArticleDetailView, name="Article-Detail"),
]
