from rest_framework import routers

class APIRoot(routers.APIRootView):
    """
    Here are all of our endpoints!
    """
    pass

class DocumentedRouter(routers.DefaultRouter):
    APIRootView = APIRoot

router = DocumentedRouter()