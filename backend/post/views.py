from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.utils.decorators import method_decorator

from groups.models import Group
from post.models import Post
from post.serializers import PostDetailSerializer, PostMinSerializer


def check_group_exists(view_func):
    def wrapper(request, *args, **kwargs):
        user_id = request.user.pk
        group_id = kwargs.get('group_id')
        try:
            Group.objects.get(id=group_id,
                              user_id=user_id)
        except Group.DoesNotExist:
            return Response(
                            {'error': 'This is not your group'},
                            status=status.HTTP_406_NOT_ACCEPTABLE
            )
        return view_func(request, *args, **kwargs)
    return wrapper


class PostViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostMinSerializer
    permission_classes = [permissions.IsAuthenticated]


    @method_decorator(check_group_exists)
    def list(self, request, group_id):
        result = Post.objects.filter(
            group_id = group_id
        )
        serializer = self.get_serializer(result, many=True)
        return Response(
            serializer.data,
        status=status.HTTP_200_OK)
    

    @method_decorator(check_group_exists)
    def create(self, request, group_id):
        if not self.check_group_existence(group_id, request.user.id):
            return Response(
            {'error': 'This is not your group'},
            status=status.HTTP_406_NOT_ACCEPTABLE
        )
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            Post.objects.create(
                group_id = group_id,
                **serializer.data
            )
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response({'error': 'Missiong required fields'},
                            status=status.HTTP_409_CONFLICT)


    def get_serializer_class(self):
        if self.action == 'list':
            return PostMinSerializer
        return PostDetailSerializer


class PostByIdViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    @method_decorator(check_group_exists)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    

    @method_decorator(check_group_exists)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    
    @method_decorator(check_group_exists)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    

    @method_decorator(check_group_exists)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)