from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from quote_api.models import Company
from content_api.models import Article
from quote_api.serializers.QuoteSerializer import QuoteSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = QuoteSerializer

    def get(self, request):
        objects = self.queryset
        serializer = self.serializer_class(objects, many=True)
        return Response(serializer.data)
    
    def get_quotes_for_article(self, request, article_id):
        article = Article.objects.get(pk=article_id)
        article_instruments = article.instruments.all()
        article_instruments_id = [instrument.instrument_id for instrument in article_instruments]

        objects = Company.objects.filter(instrumentId__in=article_instruments_id)
        serializer = self.serializer_class(objects, many=True)
        return Response(serializer.data)