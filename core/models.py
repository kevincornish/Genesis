from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
    r = models.OneToOneField(User,on_delete=models.CASCADE)
    #passkey = models.CharField("Torrent passkey", max_length=40)
    date_of_birth = models.DateField(null=True)
    def __str__(self):
        return self.r.username