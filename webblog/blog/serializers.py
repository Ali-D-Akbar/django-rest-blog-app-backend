from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Blog


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Blog
        fields = ['url', 'id', 'title', 'description', 'created', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    blog = serializers.HyperlinkedRelatedField(many=True, view_name='blog-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'blog']
