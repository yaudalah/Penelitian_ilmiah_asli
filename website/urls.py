from django.urls import path
from .views import HomeView, ArticleDetailView, AboutView, SejarahView


urlpatterns = [
    path('', HomeView, name="Home"),
    path('article/<int:post_id>', ArticleDetailView, name="Article-Detail"),
    path('sejarah-batik/', SejarahView, name="Sejarah-Batik"),
    path('about/', AboutView, name="About"),
]
