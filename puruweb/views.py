from django.shortcuts import render
from django.contrib import messages
from .models import Contact,signp
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

def logi(request):
    filter=signp.objects.all()
    n=len(filter)
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        uname=request.POST.get('Uname', '')
        pas=request.POST.get('password', '')
        # print(email,name,pas,uname)
        # print(usrName,passBro)
        if  email !="" and uname !="":
            for i in range(n):
                if email == filter[i].email :
                    messages.success(request, 'Email already exist!')
                    return render(request,'login.html')
                if uname == filter[i].userName :
                    messages.success(request, 'User Name already exist!')
                    return render(request,'login.html')
        else:
            messages.success(request, 'Your Registration Has Been Completed')
            sign_ups=signp(name=name,email=email,passwd=pas,userName=uname,date=datetime.today())
            sign_ups.save()
            return render(request,'login.html',{'name':name})
def login(request):
    filter=signp.objects.all()
    n=len(filter)
    if request.method=="POST":
        usrName=request.POST.get('user_name', '')
        passBro=request.POST.get('pass', '')
        email=request.POST.get('user_name', '')
        # print(usrName,passBro)
        if (email!="" or usrName !="") and passBro !="":
                for i in range(n):
                    if (email==filter[i].email or usrName == filter[i].userName) and passBro == filter[i].passwd:
                        messages.success(request, 'Welcome back')
                        return render(request,'login.html',{'name':filter[i].name})
                for i in range(n):
                    if (email != filter[i].email or usrName != filter[i].userName) and passBro != filter[i].passwd:
                        messages.success(request, 'No Data Found Please Sign up')
                        return render(request,'login.html')
    else:
        return render(request,'login.html')



