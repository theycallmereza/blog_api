from rest_framework import serializers
from core.models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'status', 'cdt', 'udt']
        read_only_fields = ['id']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'content', 'status', 'cdt', 'udt']
        read_only_fields = ['id']
