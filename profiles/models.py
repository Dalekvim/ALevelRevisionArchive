from django.db import models
from django.db.models import Model, OneToOneField, DateField
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse

# Create your models here.
class Profile(Model):
  user = OneToOneField(User, on_delete=models.CASCADE)
  date_of_birth = DateField(default=timezone.now)
  bio = HTMLField(default="Write a bit about yourself.")

  def get_absolute_url(self):
      return reverse("profile", kwargs={"pk": self.pk})
