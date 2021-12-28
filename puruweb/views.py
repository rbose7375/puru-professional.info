from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from datetime import datetime


# messages.success(request, 'Profile details updated.')

# Create your views here.
def main(request):
    return render(request,'main.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        subject=request.POST.get('reason', '')
        message=request.POST.get('subject', '')
        # print(name,email,phone,subject,message)
        contact=Contact(name=name,email=email,phone=phone,reason=subject,explain=message,date=datetime.now())
        contact.save()
        messages.success(request, 'Your Data Has Been Submited!')


        return render(request,'main.html')

def login(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        uname=request.POST.get('Uname', '')
        pas=request.POST.get('password', '')
        print(email,name,pas,uname)
        userName=request.POST.get('user_name', '')
        passBro=request.POST.get('pass', '')
        print(userName,passBro)
        # sign_ups=signUp(name=name,email=email,password=pas,usname=uname,date=datetime.today())
        # sign_ups.save()
        # if name !="" and email !="" and uname !="" and pas !="":


        # messages.success(request, 'Your Registration Has Been Done!')
        return render(request,'login.html')
def log(request):
    return render(request,'login.html')

