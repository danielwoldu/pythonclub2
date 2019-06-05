from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting, MeetingMinute
from .forms import ResourceForm
from django.contrib.auth.decorators import login_required


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
@login_required  
def newresource(request):
    form=ResourceForm
    if request.method=='POST':
           form=ResourceForm(request.POST)
           if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ResourceForm()
    else:
        form=ResouceForm()
    return render(request, 'clubapp/newresource.html',{'form':form})
def loginmessage(request):
    return render(request, 'clubapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'clubapp/logoutmessage.html')   
                                                                                                            
