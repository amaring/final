from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Meeting(models.Model):
    EASTERN = 'ET'
    CENTRAL = 'CT'
    MOUNTAIN = 'MT'
    PACIFIC = 'PT'
    US_TIME_ZONES = (
        (EASTERN, 'Eastern'),
        (CENTRAL, 'Central'),
        (MOUNTAIN, 'Mountain'),
        (PACIFIC, 'Pacific'),
    )
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    date = models.DateField()		#separate fields or combine date and start to make a start datetime obj?
    start = models.TimeField()
    duration = models.DurationField()
    timezone = models.CharField(max_length=2, choices=US_TIME_ZONES, default=CENTRAL)
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    repeats = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User')

    def get_absolute_url(self):
        return reverse('view_meeting', args=[self.id])
    def __str__(self):
        return self.name
"""
class user(models.Model):
    id
    first_name
    last_name
    email = model.EmailField()
    status
    timezone
    opt-in


class agenda(models.Model):
    id
    agenda_item = models.TextField()
    has_followup
    has_outcome
    has_parent

class mtg_participants
    mtg_id
    user_id

class mtg_agenda
    mtg_id
    agenda_id

class file
    id
    mtg_id
    name
"""