# App
from users.models import User
from users.serializers.create_serializers import UserCreateSerializers
from users.serializers.get_serializers import UserListSerializers
from users.serializers.update_serializers import UserUpdateSerializers

# Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializers
    permission_classes = [IsAuthenticated]
    http_method_names = ['get','head', 'put', 'delete']

    def get_queryset(self):
        queryset = self.queryset
        request = self.request
        user_request = request.user
        if not user_request.is_superuser:
            queryset = queryset.filter(pk=user_request.pk)
        return queryset

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(data='delete success')

    
    def get_serializer_class(self):
        if self.action == 'update':
            return UserUpdateSerializers
        return self.serializer_class

class UserCreatedSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializers
    http_method_names = ['post']


