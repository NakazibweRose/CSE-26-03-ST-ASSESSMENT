from django.db import models

# Create your models here.
class Video(models.Model):
    QUALITY_CHOICES = [
        ('360p', '360p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
    ]

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    quality = models.CharField(max_length=5, choices=QUALITY_CHOICES)
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.FileField(upload_to='thumbnails/')
    publishing_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publishing_date']

    def __str__(self):
        return self.title
