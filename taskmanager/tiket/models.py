from django.db import models


class Tiket(models.Model):
    owner = models.TextField()
    body = models.TextField()
    status = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body