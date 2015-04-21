from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False)

    class Meta:
        model = User
        exclude = [
            'user_permissions',
            'date_joined', 
            'groups', 
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active'
        ]

    def validate_password(self, value):
       return make_password(value)

    def validate_is_active(self, value):
       return True
