from django.shortcuts import render

# Create your views here.
def meeting_view(request):
	return render(request, 'all.html', {})