from django.urls import path, include
from rest_framework import routers

from content_api.views.ArticlesViewSet import ArticleViewSet
from content_api.views.TagViewSet import TagViewSet
from content_api.views.CommentViewSet import CommentViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'tags', TagViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls')),
    path(r'article-by-slug', ArticleViewSet.as_view({'get': 'get_by_tag_slug'})),
    path(r'submit_comment', CommentViewSet.as_view({'post': 'submit_comment'}), name='submit-comment'),
]
