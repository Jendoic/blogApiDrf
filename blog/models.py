from django.db import models
from django.contrib.auth.models import User



class Blog(models.Model):
    title = models.CharField(max_length=200,)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)
    
    def __str__(self):
        return self.title
  
    def likesCount(self):
        return self.likes.count()
    
    def commentsCount(self):
        return self.blogComment.count()
    
    
class BlogComment(models.Model):
    content = models.TextField(null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blogComment",)
    user = models.ForeignKey(User, related_name="userComment", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.blog.title} - {self.content}"
    
    def repliesCount(self):
        return self.replies.count()
    
   
    
class BlogCommentReply(models.Model):
    content = models.TextField()
    blog_comment = models.ForeignKey(BlogComment, on_delete=models.CASCADE, related_name="replies")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentReplies" )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.blog_comment.blog.title} - {self.blog_comment.content} - {self.content}"
    
