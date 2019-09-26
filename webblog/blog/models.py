from django.contrib.auth.models import User
from django.db import models, IntegrityError


class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(max_length=1500)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='blog', on_delete=models.CASCADE, null=True)
    image = models.FileField(blank=True, null=True)
    votes = models.IntegerField(default=0)

    def upvote(self, user):
        try:
            if UserVote.objects.filter(user=user, blog=self, vote_type='down').exists():
                self.post_votes.update(user=user, blog=self, vote_type='up')
                self.votes += 2

            else:
                self.post_votes.create(user=user, blog=self, vote_type='up')
                self.votes += 1

            self.save()

        except IntegrityError:
            return 'already_voted'

        return 'ok'

    def downvote(self, user):
        try:
            if UserVote.objects.filter(user=user, blog=self, vote_type='up').exists():
                self.post_votes.update(user=user, blog=self, vote_type='down')
                self.votes -= 2

            else:
                self.post_votes.create(user=user, blog=self, vote_type='down')
                self.votes -= 1

            self.save()

        except IntegrityError:
            return 'already_voted'

        return 'ok'


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


class UserVote(models.Model):
    user = models.ForeignKey('auth.User', related_name='user_votes', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='post_votes', on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10)

    class Meta:
        unique_together = ('user', 'blog', 'vote_type')
