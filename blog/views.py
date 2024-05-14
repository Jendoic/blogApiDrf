from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from django.shortcuts import get_object_or_404

from .models import Blog, BlogComment, BlogCommentReply
from .serializers import BlogSerializer, BlogCommentSerializer, BlogCommentReplySerilaizer

class BlogListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
        
class BlogDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def perform_update(self, serializer):
        blog = self.get_object()
        if blog.author!= self.request.user:
            raise PermissionDenied("You are not allowed to update this blog")
        serializer.save()
    
    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("You are not allowed to delete this blog")
        instance.delete()
        
        
class LikeUnlikeBlog(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, blog_id):
        user = request.user

        try:
            blog = Blog.objects.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response({"detail": "Blog Not Found"}, status=status.HTTP_404_NOT_FOUND)

        if blog.likes.filter(pk=user.pk).exists():
            blog.likes.remove(user)
        else:
            blog.likes.add(user)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    
class BlogCommentView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BlogCommentSerializer
    
    
    def get_queryset(self):
        blog_id = self.kwargs['blog_id']
        return BlogComment.objects.filter(blog_id=blog_id)
    
    
    def perform_create(self, serializer):
        blog_id = self.kwargs['blog_id']
        blog =  get_object_or_404(Blog, pk=blog_id)
        serializer.save(blog=blog, user=self.request.user)
        
        return Response({'detail': 'Comment created successfully'})

    
    
class BlogCommentDetails(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BlogCommentSerializer
    
    def get_queryset(self):
        blog_id = self.kwargs['blog_id']
        return BlogComment.objects.filter(blog_id=blog_id)
    

class BlogCommentReplyView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BlogCommentReplySerilaizer
    
    def get_queryset(self):
        comment_id = self.kwargs['comment_id']
        return BlogCommentReply.objects.filter(blog_comment=comment_id)
    
    def perform_create(self, serializer):
        comment_id = self.kwargs['comment_id']
        comment = get_object_or_404(BlogComment, pk=comment_id)
        serializer.save(blog_comment=comment, user=self.request.user)
        
        return Response({'detail': 'Reply created successfully'})
    