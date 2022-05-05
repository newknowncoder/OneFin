# from rest_framework import serializers
# from .models import User
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fiels = ['username', 'password']


from rest_framework import serializers

from django.contrib.auth.models import User


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'])
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
