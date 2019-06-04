from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetingagenda=models.TextField()

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'

class MeetingMinute(models.Model):
    meeting=models.ForeignKey(Meeting,on_delete=models.DO_NOTHING)
    meetingattend=models.ManyToManyField(User)
    meetingtext=models.TextField()

    def __str__(self):
        return self.meetingtext

    class Meta:
        db_table='meetingminute'    

class Resource(models.Model):
    resourceName=models.CharField(max_length=255)
    resourceType=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourceurl=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.resourceName

    class Meta:
        db_table='resource' 