from rest_framework import serializers

from groups.serializers import GroupMinSerializer
from post.models import Post


class PostMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', )


class PostDetailSerializer(serializers.ModelSerializer):
    group = GroupMinSerializer()
    class Meta:
        model = Post
        fields = ('title', 'description', 'latitude',
                  'longitude', 'group')