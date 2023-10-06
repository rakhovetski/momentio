from rest_framework import serializers

from groups.models import Group
from post.serializers import PostMinSerializer


class GroupMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title',)


class GroupDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('title', 'hex_color',)


class GroupDetailWithPostsSerializer(serializers.ModelSerializer):
    posts = PostMinSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('title', 'hex_color', 'posts')