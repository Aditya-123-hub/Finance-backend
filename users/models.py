from django.db import models
from django.contrib.auth.models import AbstractUser

ADMIN = 'admin'
ANALYST = 'analyst'
VIEWER = 'viewer'

class User(AbstractUser):
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (ANALYST, 'Analyst'),
        (VIEWER, 'Viewer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=VIEWER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


