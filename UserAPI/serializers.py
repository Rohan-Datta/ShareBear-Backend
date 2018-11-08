
from rest_framework import serializers
from UserAPI.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('displayName','email','phoneNumber','photoURL','uid')
