from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import mixins

from . import serializers


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


# class AuthenticateView(APIView):
#     def delete(self, request, format=None):
#         pass

#     def get(self, request, format=None):
#         pass

#     def post(self, request, format=None):
#         pass