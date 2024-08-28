
from django.shortcuts import render

from .models import Profile

def createProfile(request):
    profiles = Profile.objects.all()
    if request.method=='POST':
        user=request.POST.get('user')
        bio = request.POST.get('bio')
        pic= request.POST.get('image')

        profile=Profile(user=user,bio=bio,pic=pic)

        profile.save()
    return render(request,'profile.html',{'profiles':profiles})

def listProfile(request):
    profiles=Profile.objects.all()

    return render(request,'listprofile.html',{'profiles':profiles})

def index(request):
    return render(request,'index.html')