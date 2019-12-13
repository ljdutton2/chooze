from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


class User(models.Model):
    """ Represents a single wiki page. """
    username = models.CharField(max_length=120, unique=True,
                             help_text="username")
                             