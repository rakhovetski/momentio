from djoser.serializers import UserCreateSerializer
from account.models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'password')

