from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blogs_list_create'),
    path('blogs/<int:pk>/', BlogDetailUpdateDeleteView.as_view(), name='blogs_detail_update_delete'),
    path('blogs/<int:blog_id>/likeUnlike/', LikeUnlikeBlog.as_view()),
    path('blogs/<int:blog_id>/comments/', BlogCommentView.as_view()),
    path('blogs/<int:blog_id>/comments/<int:pk>/', BlogCommentDetails.as_view()),
    path('blogs/<int:blog_id>/comments/<int:comment_id>/replies/', BlogCommentReplyView.as_view()),
]
