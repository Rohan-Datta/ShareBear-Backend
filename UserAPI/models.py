from django.db import models
from django.db.models import CharField, IntegerField
from django_mysql.models import ListCharField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Authentication user model
class User(models.Model):
    displayName = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phoneNumber = models.CharField(max_length=20, null=True)
    photoURL = models.CharField(max_length=200, default='blahphoto')
    uid = models.CharField(max_length=200, default='blahuid', unique=True)

    def __str__(self):
        return '{} - {}'.format(self.email, self.displayName)

# User profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    points = models.IntegerField(default=1)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
