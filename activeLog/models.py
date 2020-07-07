from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import pytz
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))    
class activity_periods(models.Model):
    start_time =models.DateTimeField()
    end_time = models.DateTimeField()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    activity_periods = models.ManyToManyField(activity_periods,blank=True)
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
