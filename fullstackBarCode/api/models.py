from django.db import models
import string
import random

#region generate code 
def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code

#region room model
class Room(models.Model):
    #code === DCPI
    code = models.CharField(max_length=20, default="", unique=True)
    product = models.CharField(max_length=50, unique=True)
    can_add_photo = models.BooleanField(null=False, default=True)
    vote_as_damaged = models.ImageField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)


