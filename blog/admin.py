from django.contrib import admin
from .models import Blog, BlogComment, BlogCommentReply

admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(BlogCommentReply)
