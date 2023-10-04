from rest_framework.routers import DefaultRouter
from django.urls import path, include

from groups.views import GroupViewSet


router = DefaultRouter()
router.register('', GroupViewSet, basename='posts') # Create/List Group
# router.register('<int:pk>')


urlpatterns = [
    path('', include(router.urls))
]