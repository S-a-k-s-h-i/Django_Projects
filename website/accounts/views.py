from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def logging(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'First Register yourself')
            return redirect('register')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method=='POST':
       first_name=request.POST['fname']
       last_name=request.POST['lname']
       username=request.POST['username']
       email=request.POST['email']
       password1=request.POST['pass']
       password2=request.POST['repeat-pass']

       if password1==password2:
           if User.objects.filter(username=username).exists():
               messages.info(request,'Username Taken......')
               return redirect('register')
           elif User.objects.filter(email=email).exists():
               messages.info(request,"Email Taken.......")
               return redirect('register')
           else:
             user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
             user.save()
             print("user created")
             return redirect('login')
       else:
           messages.info(request,'password not matching......')
           return redirect('register')

    else:
       return render(request,'reg.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def detail_view(request):
    return render(request,'details.html')

