from rest_framework import serializers

from content_api.models import Article, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('__all__')

class ArticleSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)
    class Meta:
        model = Article
        fields = ('__all__')