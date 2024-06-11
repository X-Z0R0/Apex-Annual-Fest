from django.shortcuts import render, redirect
from .models import *    #for models importing
from django.contrib import messages  
from .utils import send_email_to_client 
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from  django.contrib.auth.decorators import login_required

 
@login_required(login_url="/login")
def landpage(request):
                              #this is the landpage
    return render(request,'Landpage.html')

#when sign up page is trigger
@csrf_protect
def signup_page(request):
    if request.method == "POST":
        _Name = request.POST.get('name')
        u_email = request.POST.get('email')
        u_college = request.POST.get('college')
        u_phoneNO = request.POST.get('phoneNO')
        password = request.POST.get('password')
        # # Check if the email already exists
        if Users_INFO.objects.filter(email=u_email).exists():
            messages.info(request, 'Email already  exist')
            return redirect('/signup/')
        elif Users_INFO.objects.filter(phoneNO=u_phoneNO).exists():
            messages.info(request, 'phone no. already exist')
            return redirect('/signup/')
        try:
            # Create a new user using your custom model
            user = Users_INFO.objects.create(name=_Name, email=u_email, college=u_college, phoneNO=u_phoneNO)
            user.set_password(password)
            user.save()
            messages.success(request, 'Account created successfully')
            send_email_to_client(user.email)
            return redirect('/login')
        except Exception as e:
            # Handle exceptions, log the error, or provide a user-friendly message
            messages.error(request, 'An error occurred during registration. Please try again.')
            # Log the exception for debugging purposes
            print(f"Error during registration: {str(e)}")
            return redirect('/signup/')
    return render(request, 'index.html',)


#when login page is trigger
@csrf_protect
def login_page(request):
    if request.method == "POST":
        u_email = request.POST.get('email')  # Assuming 'email' is the field for login
        password = request.POST.get('password')
        user = authenticate(request, email=u_email, password=password)       #it give the object if exists and if not exists then None
        a=Users_INFO.objects.filter(email=u_email)
        if not a.exists():
           messages.error(request,'Email not found')
           return redirect('/login')
        if user is None:
            messages.error(request,'password not match')
            return redirect('/login')
        else:
           login(request,user)               #login function for login in the file              
           return redirect('/landpage')
    return render(request, 'index.html',)

def logout_page(request):
    logout(request)
    return redirect('/login')