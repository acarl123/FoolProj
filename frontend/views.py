from django.shortcuts import render
from django.views.generic import TemplateView

from content_api.models import Article, Comment
from quote_api.models import Company


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['articles_list'] = Article.objects.all()

        return context

class ArticleView(TemplateView):
    template_name = 'blog-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        article = Article.objects.get(pk=self.kwargs['article_id'])
        comments = Comment.objects.filter(article=article)
        context['article'] = article
        context['company_list'] = Company.objects.all()
        context['comment_list'] = comments

        return context