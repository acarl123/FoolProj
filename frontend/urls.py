from django.urls import path, include
from frontend import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('articles/<int:article_id>', views.ArticleView.as_view(), name='article-view'),
]