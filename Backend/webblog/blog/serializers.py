from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Blog, Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    blog = serializers.HyperlinkedRelatedField(view_name='blog-detail', queryset=Blog.objects.all())

    class Meta:
        model = Comment
        fields = ['url', 'id', 'blog', 'description', 'created', 'owner']


class BlogSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['url', 'id', 'title', 'description', 'created', 'owner', 'comment']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    blog = serializers.HyperlinkedRelatedField(many=True, view_name='blog-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'blog']
