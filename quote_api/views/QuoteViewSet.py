from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from quote_api.models import Company
from quote_api.serializers.QuoteSerializer import QuoteSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = QuoteSerializer

    def get(self, request):
        objects = self.queryset
        serializer = self.serializer_class(objects, many=True)
        return Response(serializer.data)