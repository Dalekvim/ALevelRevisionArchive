from django.urls import path
from .views import UserProfile, DetailedProfile, ProfileUpdate
from django.contrib.auth.decorators import login_required

urlpatterns = [
  path('', login_required(UserProfile.as_view())),
  path('<int:pk>/', login_required(DetailedProfile.as_view()), name="profile"),
  path('<int:pk>/update/', login_required(ProfileUpdate.as_view(extra_context = {'title': 'Profile Update'})), name="profile-update"),
]
