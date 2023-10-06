from rest_framework import serializers

from post.models import Post


class PostMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', )


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'description', 'latitude',
                  'longitude',)