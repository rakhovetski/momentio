from rest_framework import serializers

from groups.models import Group


class GroupMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title',)


class GroupDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('title', 'hex_color',)