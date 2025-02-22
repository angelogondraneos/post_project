# from django.urls import path
# from . import views

# urlpatterns = [
#     # User-related URLs
#     path('users', views.user, name='user'),
#     path('users<int:user_id>', views.user_detail, name='user'),

#     # Post-related URLs
#     path('posts', views.post_list, name='post'),
#     path('posts<int:post_id>', views.post_detail, name='post'),
# ]
from django.urls import path
from . import views
from django.urls import path
from .views import UserListCreate, PostListCreate, CommentListCreate



urlpatterns = [
    # path('users/', views.get_users, name='get_users'),
    # path('users/create/', views.create_users, name='create_users'),
    # path('posts/', views.get_posts, name='get_posts'),
    path('posts/create/', views.create_posts, name='create_posts'),
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),

]
