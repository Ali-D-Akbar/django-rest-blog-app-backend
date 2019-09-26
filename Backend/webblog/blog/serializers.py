from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from blog.models import Blog, Comment


class ReplySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['parent', 'id', 'blog', 'description', 'created', 'owner']


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    blog = serializers.HyperlinkedRelatedField(view_name='blog-detail', queryset=Blog.objects.all())
    reply = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['parent', 'id', 'blog', 'description', 'created', 'owner', 'reply']

    def get_reply(self, obj):
        if obj.is_parent:
            return ReplySerializer(obj.children(), many=True).data

        return None


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['url', 'id', 'title', 'description', 'created', 'owner', 'image', 'votes', 'comment']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    blog = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'blog']
