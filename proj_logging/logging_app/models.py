from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(blank=True, null=True)