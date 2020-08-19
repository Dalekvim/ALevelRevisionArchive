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

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["search"] = self.request.GET.get('search')
    return context
  
  def get_queryset(self):
    query = self.request.GET.get('search')
    if query:
      return Post.objects.filter(title__contains=query) | Post.objects.filter(author__username__iexact=query) | Post.objects.filter(subject__iexact=query)
    return super().get_queryset()


class PostDetail(DetailView):
  model = Post


class CreatePost(CreateView):
  model = Post
  fields = ['title', 'subject', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)


class UpdatePost(UpdateView):
  model = Post
  fields = ['title', 'subject', 'content']


class DeletePost(DeleteView):
  model = Post
  success_url = '/'
