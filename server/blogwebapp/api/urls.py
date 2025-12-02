from django.urls import path
from .views import UserRegistrationView,PostList,PostDetail,CommentDetail,CommentList,CategoryList,CategoryDetail
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('posts/', PostList.as_view(), name='postlist'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='postdetails'),
    path('comments/', CommentList.as_view(),name='comment_list'),
    path('comments/<int:pk>/',CommentDetail.as_view(),name='comment_details'),
    path('categories/', CategoryList.as_view(),name='catogory_list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(),name='catogory_details'),
]