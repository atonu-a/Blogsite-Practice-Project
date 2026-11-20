from django.db import models
from shared.models import TimeStampMixin
from django.contrib.auth.models import User


class Post(TimeStampMixin):
    category_name = models.TextField(max_length=255)
# Create your models here.
