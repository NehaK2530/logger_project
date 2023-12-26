from rest_framework import serializers
from .models import Post
from datetime import datetime


class PostCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ('id','title','body','owner','created_at')

    def create(self, validated_data):
        return super().create(validated_data)

class PostUpdateSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = ('id','title','body','owner','created_at','updated_at')


    def updated(self, instance, validated_data):
        updated_at = datetime.now()
        validated_data['updated_at'] = updated_at
        return super().update(instance, validated_data)        