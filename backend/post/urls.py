from django.urls import path, include
from rest_framework.routers import DefaultRouter

from post.views import PostViewSet


app_name = 'post'


router = DefaultRouter()
router.register(r'', PostViewSet, basename='posts')


urlpatterns = [
    path('', include(router.urls)),
]