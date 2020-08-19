from django.db import models
from django.db.models import Model, CharField, ForeignKey, DateTimeField, OneToOneField, DateField
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils import timezone
from tinymce.models import HTMLField

SUBJECTS = (
  ('Further Maths', 'Further Maths'),
  ('Maths', 'Maths'),
  ('Physics', 'Physics'),
  ('Computer Science', 'Computer Science'),
  ('Japanese', 'Japanese'),
  ('Info', 'Info'),
  ('Other', 'Other'),
)

# Create your models here.
class Post(Model):
  title = CharField(max_length=150)
  author = ForeignKey(User, on_delete=models.CASCADE)
  date_posted = DateTimeField(default=timezone.now)
  subject = CharField(max_length=50, choices=SUBJECTS, default="Other")
  content = HTMLField()

  def get_absolute_url(self):
      return reverse("post", kwargs={"pk": self.pk})

