from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Note(models.Model):
  id = models.UUIDField(primary_key = True, default=uuid4, editable=False) 
  title = models.CharField(max_length = 200)
  content = models.TextField(blank = True)
  createdAt = models.DateTimeField(auto_now_add = True)
  lastModified = models.DateTimeField(auto_now = True)
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  @property
  def content_length(self):
    return len(self.content)