from django import forms
from createMeeting.models import Meeting

class CreateMeeting(forms.ModelForm):

    class Meta:
        model = Meeting
        fields = ('date','start','duration','name')
