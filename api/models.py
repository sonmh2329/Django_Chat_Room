from django.db import models

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True,null=False)
    host = models.CharField(max_length=50, unique=True, null=False)
    guest_can_pause = models.BooleanField(default=False, null=False)
    votes_to_skip = models.IntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.code
