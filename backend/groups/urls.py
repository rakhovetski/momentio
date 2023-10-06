from rest_framework.routers import DefaultRouter
from django.urls import path, include
from groups.views import GroupViewSet, GroupByIdViewSet


router = DefaultRouter()
router.register('', GroupViewSet, basename='posts'),
router.register('', GroupByIdViewSet, basename='post'),


urlpatterns = [
    path('<int:group_id>/posts/', include('post.urls')),
    path('', include(router.urls)),
]