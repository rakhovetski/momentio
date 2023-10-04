from rest_framework import viewsets

from post.models import Post
from post.serializers import PostDetailSerializer, PostMinSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostMinSerializer


    def get_serializer_class(self):
        if self.action == 'list':
            return PostMinSerializer
        return PostDetailSerializer
