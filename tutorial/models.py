from django.db import models

class Tutorial(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    tutor = models.FileField(upload_to='media/', default='video.mp4')
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title