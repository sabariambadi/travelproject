from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.



def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is  not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")
    return render(request,"login.html")

def new(request):
    if request.method== 'POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('new')
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('new')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('new')
            else:
               user=User.objects.create_user(username=username,password=password,first_name=first_name,email=email,last_name=last_name)

               user.save();
               return redirect("login")

        else:
            messages.info(request,"passwor not matching")
            return redirect('new')
        return redirect('/')


    return render(request,"man.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
