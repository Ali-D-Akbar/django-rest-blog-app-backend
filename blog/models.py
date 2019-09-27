from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(max_length=1500)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='blog', on_delete=models.CASCADE, null=True)
    image = models.FileField(blank=True, null=True)

    @property
    def votes(self):
        upvotes = UserVote.objects.filter(blog=self, vote_type='up').count()
        downvotes = UserVote.objects.filter(blog=self, vote_type='down').count()
        return upvotes - downvotes

    def upvote(self, user):
        vote, created = self.post_votes.get_or_create(user=user, blog=self)
        if not created and vote.vote_type == 'up':
            return 'already_voted'

        vote.vote_type = 'up'
        vote.save()
        return 'ok'

    def downvote(self, user):
        vote, created = self.post_votes.get_or_create(user=user, blog=self)
        if not created and vote.vote_type == 'down':
            return 'already_voted'

        vote.vote_type = 'down'
        vote.save()
        return 'ok'


class Comment(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='reply', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='comment', on_delete=models.CASCADE)
    description = models.TextField(max_length=1500)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='comment', on_delete=models.CASCADE, null=True)

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
        unique_together = ('user', 'blog')
