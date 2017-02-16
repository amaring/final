from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.meeting_view, name='meeting_view')
]