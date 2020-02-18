from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from content_api.models import Article, Tag
from content_api.serializers.ArticleSerializer import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        objects = self.queryset
        serializer = self.serializer_class(objects, many=True)
        return Response(serializer.data)
    
    def get_by_tag_slug(self, request):
        slug = self.request.query_params.get('slug', None)
        tags = Tag.objects.filter(slug=slug)
        if not tags:
            return HttpResponse({"error": "no matching article found"})
        
        objects = Article.objects.filter(tags__in=tags)
        serializer = self.serializer_class(objects, many=True)
        return Response(serializer.data)