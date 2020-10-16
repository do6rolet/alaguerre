from django.db import models

from django.contrib.auth.models import User


class Report(models.Model):
    body = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='reports', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)  # '-created_at' - give reversed ordering


class Like(models.Model):
    report = models.ForeignKey(Report, related_name='likes', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

