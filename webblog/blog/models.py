from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=1500)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='blog', on_delete=models.CASCADE, null=True)

