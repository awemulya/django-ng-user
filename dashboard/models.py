from django.db import models

class Players(models.Model):
    name = models.CharField(max_length=255,verbose_name="name")
    date_of_birth = models.DateField()
