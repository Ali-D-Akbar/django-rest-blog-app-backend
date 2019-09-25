from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from blog.models import Blog, Comment
from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import BlogSerializer, UserSerializer, CommentSerializer


class BlogAPI(viewsets.ModelViewSet):
    queryset = Blog.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(created=timezone.now())

    def list(self, request, *args, **kwargs):
        if request.GET.get('keyword', '') != '':
            queryset = Blog.objects.filter(title__icontains=request.GET.get('keyword'),
                                           description__contains=request.GET.get('keyword'))
        else:
            queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentAPI(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
