from django.db import models
from UserAPI.models import User
from django.utils import timezone
from datetime import date
from django.db import models
from django import forms

#Entry Type Variable Names
MOVIE = "Movie"
TV = "TV Show"
GAME = "Games"
STUFF = "Stuff"
SERVICE = "Service"

#Entry Choices
ENTRY_TYPES = ((MOVIE, "Movie"), (TV, "TV Show"), (GAME, "Games"), (STUFF, "Stuff"), (SERVICE, "Service"))

# Entry model
class Entry(models.Model):
    name = models.CharField(max_length=200)
    posted_by = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    entry_type = models.CharField(max_length=10, choices=ENTRY_TYPES, null=False)
    tags = models.CharField(max_length=100, null=True)
    
    #Overiding Save Function to Automatically input DateTime
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Entry, self).save(*args, **kwargs)
        
    def __str__(self):
        return '{} - {}'.format(self.name, self.posted_by)