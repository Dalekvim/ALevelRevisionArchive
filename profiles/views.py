from django.shortcuts import render
from django.views.generic import (
  DetailView,
  TemplateView,
  UpdateView,
)

from .models import Profile
from django.contrib.auth.models import User


# Create your views here.
class UserProfile(TemplateView):
  model = User
  template_name = "accounts/profile.html"


class DetailedProfile(DetailView):
  model = User
  template_name = "accounts/profile.html"


class ProfileUpdate(UpdateView):
  model = Profile
  fields = ['date_of_birth', 'bio']