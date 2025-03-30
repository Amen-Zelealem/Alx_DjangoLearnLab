from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()  
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})  
    bio = serializers.CharField(required=False, allow_blank=True) 
    profile_picture = serializers.ImageField(required=False)  

    def create(self, validated_data):
        if get_user_model().objects.filter(username=validated_data['username']).exists():
            raise ValidationError("Username already exists.")
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None),
        )
        Token.objects.create(user=user)
        return user
