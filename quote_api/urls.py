from django.urls import path, include

from quote_api.custom_router import DocumentedRouter
from quote_api.views.QuoteViewSet import QuoteViewSet

router = DocumentedRouter()
router.register(r'quotes', QuoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls')),
]
