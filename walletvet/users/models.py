from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# OBS: This is the user/owner model

class User(AbstractBaseUser):
    name = models.CharField('Name', max_length=100, null=False, blank=False)
    email = models.EmailField('Email', max_length=100, unique=True)
    is_active = models.BooleanField('active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return super().__str__() 