"""
Routing configuration for the locations application.
"""

from rest_framework import routers

from .views import LocationsViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register("locations", LocationsViewSet)

urlpatterns = router.urls
