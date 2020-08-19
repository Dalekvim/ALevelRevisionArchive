from django.shortcuts import render
from django.views.generic import FormView

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class CreateUser(FormView):
  template_name = "registration/register.html"
  form_class = UserCreationForm
  success_url = '/accounts/login/'

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)
