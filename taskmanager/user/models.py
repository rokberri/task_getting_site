from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.TextField(primary_key=True, max_length = 32)
    email = models.EmailField(blank=True)
    password = models.TextField

    def __str__(self) -> str:
        return self.user_name