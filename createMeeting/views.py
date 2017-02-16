from django.shortcuts import render, redirect
from django.http import HttpResponse
from createMeeting.models import Meeting


# Create your views here.
def home_page(request):
    return render(request, 'meeting.html')

def new_meeting(request, meeting_id):
    meeting_ = Meeting.objects.get(id=meeting_id)
    if request.method == 'POST':

        meetingTitle = request.POST.get('meeting_title', '')
        startDate = request.POST.get('start_date')
        startTime = request.POST.get('start_time')
        duration = request.POST.get('duration')
        #participants = request.POST.get('participants')
        #agenda = request.POST.get('agenda')

        meeting_obj = Meeting(date = startDate, start = startTime, duration = duration,  name = meetingTitle)
        Meeting.objects.create(meeting_obj)
        return redirect('/meeting/%d' % (meeting_.id,))


'''def view_meeting(request):
    meeting_ = Meeting.objects.get(id=meeting_id)
    return render(request, 'meeting.html', {'meeting': meeting_})

'''


