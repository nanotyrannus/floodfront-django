from django.db import models

# Create your models here.
class Marker(models.Model):
    lon = models.FloatField(default=0)
    lat = models.FloatField(default=0)
    heading = models.FloatField(null=True)
    is_directional = models.BooleanField(default=False)
    accuracy = models.FloatField(default=-1)
    description = models.TextField(default="")
    created_on = models.DateField(auto_now=True) # updated whenever instance is modified
    marker_type = models.TextField(null=False)
    email = models.EmailField(null=False)

# Akin to a "guest" account, tied only to email
# created upon login
class User(models.Model): 
    email = models.EmailField(null=False)