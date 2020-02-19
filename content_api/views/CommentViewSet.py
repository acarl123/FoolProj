from rest_framework import viewsets
from rest_framework.response import Response
import json

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse

from content_api.models import Comment
from content_api.serializers.CommentSerializer import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def submit_comment(self, request):
        data = request.data
        comment = Comment(name=data['name'], message=data['message'], article_id=data['article'])
        comment.save()
        return redirect('/articles/{}'.format(data['article']))