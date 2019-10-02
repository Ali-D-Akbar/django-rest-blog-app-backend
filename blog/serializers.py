from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

<<<<<<< HEAD
from blog.models import Blog, Comment, UserVote


class ReplySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

=======
from blog.models import Blog, Comment


class ReplySerializer(serializers.ModelSerializer):
>>>>>>> master
    class Meta:
        model = Comment
        fields = ['parent', 'id', 'blog', 'description', 'created', 'owner']


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
<<<<<<< HEAD
    blog = serializers.HyperlinkedRelatedField(
        view_name='blog-detail',
        lookup_field='slug',
        queryset=Blog.objects.all()
    )
=======
    blog = serializers.HyperlinkedRelatedField(view_name='blog-detail', queryset=Blog.objects.all())
>>>>>>> master
    reply = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['parent', 'id', 'blog', 'description', 'created', 'owner', 'reply']

    def get_reply(self, obj):
        if obj.is_parent:
            return ReplySerializer(obj.children(), many=True).data
<<<<<<< HEAD

=======
>>>>>>> master
        return None


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
<<<<<<< HEAD
        fields = ['url', 'slug', 'id', 'title', 'description', 'created', 'owner', 'image', 'votes', 'comment', 'draft']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
=======
        fields = ['url', 'id', 'title', 'description', 'created', 'owner', 'image', 'comment']
>>>>>>> master


class UserSerializer(serializers.HyperlinkedModelSerializer):
    blog = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'blog']
<<<<<<< HEAD


class VoteSerializer (serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    blog = serializers.HyperlinkedRelatedField(
        view_name='blog-detail',
        lookup_field='slug',
        queryset=Blog.objects.all()
    )

    class Meta:
        model = UserVote
        fields = ['url', 'id', 'user', 'blog', 'vote_type']
=======
>>>>>>> master
