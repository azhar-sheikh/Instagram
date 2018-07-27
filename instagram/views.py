from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Image, Profile
import datetime as dt
from django.contrib.auth import logout
from .forms import NewImageForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    date = dt.date.today()
    image = Image.get_all()
    return render(request, 'index.html', {"image":image})

def logout(request):
    logout(request)
    return render(request, 'login.html')

def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.user = current_user
            image.save()
    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request, user_id):
        date = dt.date.today()
        profile = Profile.objects.filter(user_id = profile_id).first()
        image = Image.objects.filter(user_id=request.user.id)


    return render(request, 'profile.html', locals())
