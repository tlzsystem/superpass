from django.db import models
from django.contrib.auth.models import User

class Servicio(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name