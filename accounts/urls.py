from django.urls import path
from .views import CreateUser
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
  path('register/', CreateUser.as_view(extra_context = {'title': 'Sign Up'}), name='register'),
  path('login/', LoginView.as_view(extra_context = {'title': 'Login'}), name='login'),
  path('logout/', LogoutView.as_view(extra_context = {'title': 'Logout'}, template_name="registration/logout.html"), name='logout'),
]
