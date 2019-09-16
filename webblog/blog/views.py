from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from blog.models import Blog
from blog.serializers import BlogSerializer, UserSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = BlogSerializer

    def get_queryset(self):
        return self.request.user.blog.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
