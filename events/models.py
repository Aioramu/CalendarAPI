from django.db import models
from authorization.models import User
# Create your models here.
class Holidays(models.Model):
    country=models.CharField(max_length=255,unique=True)
    day=models.DateField(auto_now=False)

class Events(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,to_field='email')
    summary=models.CharField(max_length=255)
    time_from=models.DateTimeField(auto_now=False)
    time_to=models.DateTimeField(auto_now=False)
    NOTIFICATIONS=[
    ('За час', 1),
    ('За два часа', 2),
    ('За 4 часа', 4),
    ('За день', 24),
    ('За неделю', 168),
    ]#e.get_notification_display()
    notification=models.CharField(max_length=255,choices=NOTIFICATIONS,null=True,default=None)
