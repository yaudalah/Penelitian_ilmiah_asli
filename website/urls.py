from django.urls import path
from .views import HomeView, ArticleDetailView, About

urlpatterns = [
    # path('', HomeView.as_view(), name="home"),
    path('', HomeView, name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="Article-Detail"),
]
