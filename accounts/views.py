from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from accounts.models import Register, UserInfo
from django.conf import settings
import os

def register_view(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        
        if email and mobile and password:
            hashed_password=make_password(password)
            Register.objects.create(
                email=email,
                mobile=mobile,
                password=hashed_password,
            )
        return redirect('info')
    
    register_info=Register.objects.all()
    return render(request, "register.html", {'register': register_info})

def login_view(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        try:
            user=Register.objects.get(email=email)
            
            if check_password(password, user.password):
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
        except:
            messages.error(request, 'User not found, Please register!')
            return redirect('register')
    return render(request, 'login.html')


def user_info(request):
    if request.method == 'POST':
        fname=request.POST.get('fullname')
        age=request.POST.get('age')
        height=request.POST.get('height')
        weight=request.POST.get('weight')
        working=request.POST.get('working')
        whours=request.POST.get('working_hours')
        
        if fname and age and height and weight and working and whours:
            UserInfo.objects.create(
                fullname=fname,
                age=age,
                height=height,
                weight=weight,
                working=working,
                working_hours=whours
            )
        
        return redirect('dashboard')
    userinfo=UserInfo.objects.all()
    return render(request, 'info.html', {'info':userinfo})   

def user_info_show(request):
    show_info=UserInfo.objects.all()
    return render(request, 'user_info.html', {'show_info':show_info} )


def flipbook_view(request):
    return render(request, 'flipbook.html')

