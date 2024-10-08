from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=50)
    content = models.TextField(verbose_name="Content")
    link = models.TextField(verbose_name="Link", max_length=300)
    imagen = models.FileField(null=True, blank=True, upload_to='images')
    video = models.FileField(null=True, blank=True, upload_to='video')
    audio = models.FileField(null=True, blank=True, upload_to='audio')
    pdf = models.FileField(null=True, blank=True, upload_to='pdf')
    time_created = models.DateTimeField(auto_now=True)
    time_last_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title