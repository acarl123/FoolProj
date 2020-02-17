from django.urls import path, include

from quote_api.custom_router import DocumentedRouter

router = DocumentedRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls')),
]
