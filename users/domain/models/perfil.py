from django.db import models

class Perfil(models.Model):
    nick_name = models.CharField(max_length=250)