from rest_framework import serializers

from quote_api.models import Company


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('__all__')