from django.shortcuts import render
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView,
)

from .models import Post
from django.contrib.auth.models import User


# Create your views here.
class PostList(ListView):
  model = Post
  ordering = ['-date_posted']


class PostDetail(DetailView):
  model = Post


class CreatePost(CreateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)


class UpdatePost(UpdateView):
  model = Post
  fields = ['title', 'content']


class DeletePost(DeleteView):
  model = Post
  success_url = '/'
