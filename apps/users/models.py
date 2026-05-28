from django.db import models
from apps.permissions_system.models import Role


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=255)

    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email