from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Doctor
#import messages
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login



# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            doctor = Doctor.objects.get(user=user)
            if doctor.verify == True:
                auth_login(request, user)
                return render(request, 'home.html')
            else:
                messages.error(request, 'Please wait for approval')
                return render(request, 'register/login.html')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'register/login.html')
            

        
        
    return render(request, 'register/login.html')



def register(request):
    if request.method == 'POST':
        if 's1' in request.POST:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            password1 = request.POST.get('password1')
            if User.objects.filter(username=email).exists():
                messages.error(request, 'Email already exists')
                return render(request, 'register/register.html')
            elif password != password1:
                messages.error(request, 'Passwords do not match')
                return render(request, 'register/register.html')
            else:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                doctor = Doctor(user=user, fname=fname, lname=lname, email=email, phone=phone)
                doctor.save()
                return render(request, 'register/moreinfo.html',{'email':email})
        elif 's2' in request.POST:
            verify = request.POST.get('verify')
            registration_number = request.POST.get('rnumber')
            specialization = request.POST.get('specialization')
            hospital_name = request.POST.get('hname')
            hospital_address = request.POST.get('haddress')
            hospital_phone = request.POST.get('hphnum')
            hospital_email = request.POST.get('hemail')
            hospital_pincode = request.POST.get('hpin')
            hospital_city = request.POST.get('hcity')
            doctor = Doctor.objects.get(email=verify)
            doctor.registration_number = registration_number
            doctor.specialization = specialization
            doctor.hospital_name = hospital_name
            doctor.hospital_address = hospital_address
            doctor.hospital_phone = hospital_phone
            doctor.hospital_email = hospital_email
            doctor.hospital_pincode = hospital_pincode
            doctor.hospital_city = hospital_city
            doctor.save()
            return render(request, 'register/confirmpage.html')
    return render(request, 'register/register.html')

def approve(request):
    return render(request, 'administration/approve.html')