from django.urls import path
from . import views
from .views import DownloadResumeView
urlpatterns=[
    path('',views.index,name='index'),
    path('resume_view',DownloadResumeView.as_view(),name='resume_view')
]