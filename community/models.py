from django.db import models
from users.models import CustomUser

class Community(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default='Title')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='media', default='none.png')

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.community.title}"