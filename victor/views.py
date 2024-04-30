
from django.shortcuts import render
import os
from django.conf import settings
from django.http import FileResponse
from django.views import View
from .models import Home, About, Profile, Category, Skills, Portfolio

def index(request):
    home = Home.objects.latest('updated')
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)
    categories = Category.objects.all()
    portfolios = Portfolio.objects.all()
    context = {
        'home': home,
        'about': about,
        'categories': categories,
        'profiles':profiles,
        'portfolios': portfolios
    }
    return render(request, 'victor/index.html', context)

class DownloadResumeView(View):
    def get(self,request,*args,**kwargs):
        resume_path=os.path.join(settings.MEDIA_ROOT,'pdf/resume.pdf')
        return FileResponse(open(resume_path,'rb'),content_type='application/pdf')


