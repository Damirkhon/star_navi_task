from django.utils import timezone
from .models import Post, Profile, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
            "email"
        ]
        write_only_fields = ("password",)
        read_only_fields = ("id",)
    
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(user=user, last_activity=timezone.now())
        return user


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "author",
        ]