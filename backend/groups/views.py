from rest_framework import viewsets
from rest_framework import mixins

from groups.serializers import GroupDetailSerializer, GroupMinSerializer
from groups.models import Group


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return GroupMinSerializer
        return GroupDetailSerializer
    

class GroupViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupMinSerializer


    def get_serializer_class(self):
        if self.action == 'list':
            return GroupMinSerializer
        return GroupDetailSerializer