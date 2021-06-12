from django.db import models
from .user import User


class Supervisor(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supervisor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name.first_name} {self.name.last_name}'
