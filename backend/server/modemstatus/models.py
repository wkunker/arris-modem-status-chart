from django.db import models

class ModemStatus(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status_data = models.CharField(max_length=20000, blank=False)
    weather_data = models.CharField(max_length=20000, blank=False)

