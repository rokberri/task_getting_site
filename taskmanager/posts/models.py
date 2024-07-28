from django.db import models


class Post(models.Model):
    title = models.CharField(max_length= 128)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self) -> str:
        return self.title