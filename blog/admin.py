from django.contrib import admin

<<<<<<< HEAD
from blog.models import Blog, Comment, UserVote

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(UserVote)
=======
from blog.models import Blog, Comment


admin.site.register(Blog)
admin.site.register(Comment)
>>>>>>> master
