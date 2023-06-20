from django.shortcuts import render, redirect
from .models import Profile, User
from .mixins import send_otp
from random import randint
# Create your views here.

def register(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        username = request.POST.get('username')
        user = User.objects.create(phone_number = phone_number, username = username)
        profile = Profile.objects.create(username =  user, phone_number = phone_number)
        profile.save()
        return redirect('login_view')
    return render(request, 'register.html')
       
        
def login_view(request):

    
    if request.POST:
        phone_number = request.POST.get('phone_number')
        try:
            profile = Profile.objects.filter(phone_number = phone_number)
            if profile.exists():
                redirect('register')
            else:
                profile[0].otp = randint(1000, 9999)
                send_otp(phone_number, profile[0].otp)
                profile[0].save()
                return redirect('otp/{profile[0].uid}')

        except Exception as e:
            print(e)
        