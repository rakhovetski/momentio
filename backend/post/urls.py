from django.urls import path, include
from rest_framework.routers import DefaultRouter

from post.views import PostViewSet, PostByIdViewSet


app_name = 'post'


router = DefaultRouter()
router.register('', PostViewSet, basename='posts')
router.register('', PostByIdViewSet, basename='post')


urlpatterns = [
    path('', include(router.urls)),
]