from typing import Any
from django.db import models
import datetime


class Tiket(models.Model):
    owner = models.TextField()
    body = models.TextField()
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body
 

