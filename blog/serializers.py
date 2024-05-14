from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Blog, BlogComment, BlogCommentReply

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username')

class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    likes = UserSerializer(many=True, read_only=True)
    likeCount = serializers.SerializerMethodField()
    commentsCount = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = "__all__"
        
    def get_likeCount(self, object):
        return object.likesCount()
    
    def get_commentsCount(self, object):
        return object.commentsCount()
    
    
class BlogCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    blog = serializers.PrimaryKeyRelatedField(read_only=True)
    repliesCount = serializers.SerializerMethodField()
    class Meta:
        model = BlogComment
        fields = "__all__"
        
        
    def get_repliesCount(self, object):
        return object.repliesCount()
    
        
class BlogCommentReplySerilaizer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    blog_comment = serializers.PrimaryKeyRelatedField(read_only=True)
    repliesCount = serializers.SerializerMethodField()
    class Meta:
        model = BlogCommentReply
        fields = "__all__"
        
    