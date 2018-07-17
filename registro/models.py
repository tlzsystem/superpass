from django.db import models
from servicio.models import Servicio

class Registro(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    reg_user = models.CharField(max_length=100)
    reg_pass = models.CharField(max_length=100)

    def __str__(self):
        return self.servicio.name