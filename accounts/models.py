from django.db import models

from django.contrib.auth.models import User


class NovusUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # some privileges
