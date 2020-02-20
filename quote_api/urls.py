from django.urls import path, include

from quote_api.custom_router import DocumentedRouter
from quote_api.views.QuoteViewSet import QuoteViewSet

router = DocumentedRouter()
router.register(r'quotes', QuoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls')),
    path(r'quotes-per-article/<int:article_id>', QuoteViewSet.as_view({'get': 'get_quotes_for_article'}), name='quotes-per-article'),
]
