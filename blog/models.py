from django.db import models
from django.utils import timezone

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'dr', 'Draft'
        PUBLISHED = 'pu', 'Published'
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField()
    published = models.DateTimeField(default=timezone.now)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
