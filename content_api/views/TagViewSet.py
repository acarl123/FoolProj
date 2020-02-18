from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from content_api.models import Tag
from content_api.serializers.ArticleSerializer import ArticleSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, pk):
        if pk:
            objects = get_object_or_404(Tag, pk=pk)
        else:
            objects = queryset
            
        serializer = self.serializer_class(objects, many=True)
        return Response(serializer.data)