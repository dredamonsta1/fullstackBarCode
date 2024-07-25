from django.db import models

# Create your models here.
class Room(models.Model):
    #code === DCPI
    code = models.charField(max_length=20, default="", unique=True)
    product = models.CharField(max_length=50, unique=True)
    can_add_photo = models.BooleanField(null=False, default=True)
    vote_as_damaged = models.ImageField(null=False, default=1)


