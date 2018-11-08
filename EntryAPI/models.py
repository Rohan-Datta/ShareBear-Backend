from django.db import models
from UserAPI.models import Profile

# Entry model
class Entry(models.Model):
    name = models.CharField(max_length=200)
    posted_by = models.ForeignKey(Profile, default=None, on_delete=models.CASCADE)

#    creationTime = models.CharField(max_length=20)

    def __str__(self):
        return '{} - {}'.format(self.name, self.posted_by)
