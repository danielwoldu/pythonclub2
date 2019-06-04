from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting, MeetingMinute

# Create your views here.
def index (request):
    return render(request, 'clubapp/index.html')

def getresource(request):
    resources=Resource.objects.all()
    return render(request,'clubapp/resources.html',{'resources':resources})    

def getmeeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'clubapp/meeting.html', {'meeting_list': meeting_list})

def getmeetingdetail(request,id):
    meeting=get_object_or_404(Meeting,pk=id)
    return render(request,'clubapp/detail.html',{'meeting':meeting})
    