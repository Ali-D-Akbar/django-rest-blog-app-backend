from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(max_length=1500)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='blog', on_delete=models.CASCADE, null=True)


class CommentManager(models.Manager):
    def all(self):
        comments = super(CommentManager, self).filter(parent=None)
        return comments


class Comment(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='reply', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='comment', on_delete=models.CASCADE)
    description = models.TextField(max_length=1500)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='comment', on_delete=models.CASCADE, null=True)
    objects = CommentManager()

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
