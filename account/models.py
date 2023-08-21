from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username",]

    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='media/users/')

    
    
