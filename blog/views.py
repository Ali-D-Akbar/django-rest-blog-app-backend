from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from rest_framework import viewsets, permissions
<<<<<<< HEAD
from rest_framework.decorators import action
from rest_framework.response import Response

from blog.models import Blog, Comment, UserVote
from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import BlogSerializer, UserSerializer, CommentSerializer, VoteSerializer
=======
from rest_framework.response import Response

from blog.models import Blog, Comment
from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import BlogSerializer, UserSerializer, CommentSerializer
>>>>>>> master


class BlogAPI(viewsets.ModelViewSet):
    queryset = Blog.objects.all()

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]
<<<<<<< HEAD
    lookup_field = 'slug'
=======
>>>>>>> master

    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(created=timezone.now())

    def list(self, request, *args, **kwargs):
        if request.GET.get('keyword', '') != '':
            queryset = Blog.objects.filter(
                Q(title__icontains=request.GET.get('keyword')) |
                Q(description__contains=request.GET.get('keyword'))
            )
<<<<<<< HEAD

=======
>>>>>>> master
        else:
            queryset = Blog.objects.all()

        serializer = BlogSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

<<<<<<< HEAD
    @action(detail=True)
    def upvote(self, request, *args, **kwargs):
        blog = self.get_object()
        return Response(blog.upvote(request.user))

    @action(detail=True)
    def downvote(self, request, *args, **kwargs):
        blog = self.get_object()
        return Response(blog.downvote(request.user))

=======
>>>>>>> master

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentAPI(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
<<<<<<< HEAD
=======

>>>>>>> master
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
<<<<<<< HEAD


class VoteAPI(viewsets.ModelViewSet):
    queryset = UserVote.objects.all()
    serializer_class = VoteSerializer
=======
>>>>>>> master
