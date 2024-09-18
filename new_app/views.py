
from django.shortcuts import render,redirect

from .models import Profile


def createProfile(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        bio = request.POST.get('bio')
        image = request.FILES.get('image')

        Profile.objects.create(user=user, bio=bio, image=image)

        return redirect('listprofile')

    profiles = Profile.objects.all()
    return render(request, 'profile.html', {'profiles': profiles})

def listProfile(request):
    profiles=Profile.objects.all()

    return render(request,'listprofile.html',{'profiles':profiles})

def index(request):
    return render(request,'index.html')

