from django.db import models

class application(models.Model):
    title = models.CharField(max_length=255)

class apikey(models.Model):
    key = models.CharField(max_length=255)
