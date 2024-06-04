from django.db import models
from django.utils import timezone

class Post(models.Model):
  class Status(models.TextChoices):
    DRAFT = 'DF', 'Draft'
    PUBLISHED = 'PB', 'Published'
    
  title = models.CharField(max_length=200)

  publish = models.DateTimeField(default=timezone.now)

  class Meta:
    ordering = ['-publish']
    indexes = [
      models.Index(fields=['publish']),
    ]
    

  def __str__(self):
    return self.title