from django.db import models

class todoDB(models.Model):
    item = models.CharField(max_length=100)
