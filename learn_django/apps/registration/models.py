from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
import smtplib

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=True)
    study_group = models.PositiveIntegerField(default = 0)
    progress = models.CharField(max_length=200, default= 'none')

    def SendVerify(self):
        server = smtplib.SMTP_SSL('smtp.yandex.com')
        email = 'maksim.astash@yandex.ru'
        password = 'Ofezum412002Takatoma2323'
        server.set_debuglevel(1)
        server.ehlo(email)
        server.login(email, password)
        server.auth_plain()
        BODY = "\r\n".join((
            "From: %s" % email,
            "To: %s" % self.user.email,
            "Subject: %s" % 'Activate account',
            "",
            "127.0.0.1:8000/verify/%s" % str(self.uuid)
        ))
        server.sendmail(email, self.user.email, BODY)
        server.quit()

    def __str__(self):
        return self.user.username
    
   