from django.urls import path
from .views import PostList, PostDetail, CreatePost, UpdatePost, DeletePost
from django.contrib.auth.decorators import login_required

urlpatterns = [
  path('', PostList.as_view(extra_context = {'title': 'Blog Home'}), name='home'),
  path('<int:pk>/', PostDetail.as_view(extra_context = {'title': 'Post Detail'}), name='post'),
  path('create/', login_required(CreatePost.as_view(extra_context = {'title': 'Create'})), name='create'),
  path('<int:pk>/update/', login_required(UpdatePost.as_view(extra_context = {'title': 'Update'})), name='update'),
  path('<int:pk>/delete/', login_required(DeletePost.as_view(extra_context = {'title': 'Delete'})), name='delete'),
]
