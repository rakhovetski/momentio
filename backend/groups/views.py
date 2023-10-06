from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from groups.serializers import GroupDetailSerializer, GroupMinSerializer, GroupDetailWithPostsSerializer
from groups.models import Group

    

class GroupViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Group.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GroupMinSerializer


    def list(self, request):
        user_id = request.user.id
        groups = Group.objects.filter(
            user_id=user_id
        )
        serailizer = self.get_serializer_class(groups, many=True)
        return Response(
            serailizer.data,
            status=status.HTTP_200_OK
        )


    def create(self, request):
        user_id = request.user.id
        title = request.data.get('title')
        hex_color = request.data.get('hex_color')

        if not all([title, hex_color]):
            return Response({'error': 'Missiong required fields'},
                            status=status.HTTP_409_CONFLICT)
        
        group = Group.objects.create(user_id=user_id,
                                     title=title,
                                     hex_color=hex_color)
        serializer = self.get_serializer_class(group)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
            

    def get_serializer_class(self):
        if self.action == 'list':
            return GroupMinSerializer
        return GroupDetailSerializer
    

class GroupByIdViewSet(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return GroupDetailWithPostsSerializer
        return GroupDetailSerializer
    