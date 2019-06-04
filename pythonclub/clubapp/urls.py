from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getresources/',views.getresource,name='resources'),
    path('getmeeting/',views.getmeeting,name='meeting'),
    path('getmeetingdetail/<int:id>',views.getmeetingdetail,name='details')
   
]