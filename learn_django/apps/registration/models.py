from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    study_group = models.PositiveIntegerField(default = 0)
    progress = models.CharField(max_length=200, default= 'none')
    def __str__(self):
        return self.user.username