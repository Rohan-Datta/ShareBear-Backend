from django.db import models

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
    displayName = models.CharField(max_length=200)
