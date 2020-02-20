from rest_framework import serializers

from content_api.models import Article, Image, Instrument


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('__all__')


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('__all__')


class ArticleSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)
    instruments = InstrumentSerializer
    class Meta:
        model = Article
        fields = ('__all__')