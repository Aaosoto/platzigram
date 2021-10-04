"""User models"""

from django.contrib.auth.models import User, update_last_login
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

class Profile(models.Model):
    """Proxy model.
    
    Proxy model that extends the base data with other information.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to = 'user/pictures', blank = True, null = True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username