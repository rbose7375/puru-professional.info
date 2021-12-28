from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

# from django.http import HttpResponse
from django.contrib import messages
<<<<<<< HEAD
<<<<<<< HEAD
from .models import Contact, signp, personal,gallary
=======
from .models import Contact,signp
>>>>>>> 2155350 (working now long signup contact)
=======
from .models import Contact, signp, personal
>>>>>>> 02329d5 (tatti gallary)
from datetime import datetime


# messages.success(request, 'Profile details updated.')

# Create your views here.
def main(request):
    return render(request, 'main.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('reason', '')
        message = request.POST.get('subject', '')
        # print(name,email,phone,subject,message)
        contact = Contact(name=name, email=email, phone=phone,
                          reason=subject, explain=message, date=datetime.now())
        contact.save()
        messages.success(request, 'Your Data Has Been Submited!')

        return render(request, 'main.html')
<<<<<<< HEAD


def logi(request):
    filter = signp.objects.all()
    n = len(filter)
    print(n)
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        uname = request.POST.get('Uname', '')
        pas = request.POST.get('password', '')
        print(email, name, pas, uname)
        if email != "" and uname != "":
            for i in range(n):

                if email == filter[i].email:
                    messages.success(request, 'Email already exist!')
                    print(email, name, pas, uname)
                    return render(request, 'login.html')

                if uname == filter[i].userName:
                    messages.success(request, 'User Name already exist!')
                    print(email, name, pas, uname)
                    return render(request, 'login.html')

            messages.success(request, 'Your Registration Has Been Completed')
            print(email, name, pas, uname)
            sign_ups = signp(name=name, email=email, passwd=pas,
                             userName=uname, date=datetime.today())
            sign_ups.save()
            return render(request, 'login.html', {'name': name})


<<<<<<< HEAD
def login(request):
    filter = signp.objects.all()
    n = len(filter)
    if request.method == "POST":
        usrName = request.POST.get('user_name', '')
        passBro = request.POST.get('pass', '')
        email = request.POST.get('user_name', '')
        # print(usrName,passBro)
        if (email != "" or usrName != "") and passBro != "":
                for i in range(n):
                    if (email == filter[i].email or usrName == filter[i].userName) and passBro == filter[i].passwd:
                        messages.success(request, 'Welcome back')
                        return render(request, 'login.html', {'name': filter[i].name})

                messages.success(request, 'No Data Found Please Sign up')
                return render(request, 'login.html')
    return render(request, 'login.html')


def home(request):
    datas = signp.objects.all()
    return render(request, 'home.html', {'info': datas})


def homes(request):
    datas = signp.objects.all()
    messages.success(request, 'Update Successfully! bro')
    return render(request, 'home.html', {'info': datas})


def deleteData(request, id):
    if request.method == 'POST':
        data = signp.objects.get(pk=id)
        print(data)
        data.delete()
        return HttpResponseRedirect('/home')


def update(request, id):
    if request.method == 'POST':
        data = signp.objects.get(pk=id)
        print(data)
        return render(request, 'update.html', {'info': data})
# def upda(request):


def updat(request, id):
        data = signp.objects.get(pk=id)
        if request.method == 'POST':
            data.name = request.POST.get('name', '')
            data.email = request.POST.get('email', '')
            data.userName = request.POST.get('Uname', '')
            data.passwd = request.POST.get('password', '')
            datas = {
                'name': data.name,
                'email': data.email,
                'userName': data.userName,
                'passwd': data.passwd,
            }
            print(datas)
            data.save()
            return HttpResponseRedirect('/homes')


def Personal(request):
    details = personal.objects.all()
    n = len(details)
   
   

    params={'detail':details,'deta':details,'detai':details}

    return render(request,'personal.html',params)

def gallarys(request):

    return render(request,'gallary.html')


def img(request):
    allimg=gallary.objects.all()
    print(allimg)
    params={'data':allimg}
    return render(request,'common.html',params)
=======

>>>>>>> 02329d5 (tatti gallary)

=======
def logi(request):
    filter = signp.objects.all()
    n = len(filter)
    print(n)
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        uname = request.POST.get('Uname', '')
        pas = request.POST.get('password', '')
        print(email, name, pas, uname)
        if email != "" and uname != "":
            for i in range(n):

                if email == filter[i].email:
                    messages.success(request, 'Email already exist!')
                    print(email, name, pas, uname)
                    return render(request, 'login.html')

                if uname == filter[i].userName:
                    messages.success(request, 'User Name already exist!')
                    print(email, name, pas, uname)
                    return render(request, 'login.html')

            messages.success(request, 'Your Registration Has Been Completed')
            print(email, name, pas, uname)
            sign_ups = signp(name=name, email=email, passwd=pas,
                             userName=uname, date=datetime.today())
            sign_ups.save()
            return render(request, 'login.html', {'name': name})


def login(request):
    filter = signp.objects.all()
    n = len(filter)
    if request.method == "POST":
        usrName = request.POST.get('user_name', '')
        passBro = request.POST.get('pass', '')
        email = request.POST.get('user_name', '')
        # print(usrName,passBro)
        if (email != "" or usrName != "") and passBro != "":
                for i in range(n):
                    if (email == filter[i].email or usrName == filter[i].userName) and passBro == filter[i].passwd:
                        messages.success(request, 'Welcome back')
<<<<<<< HEAD
                        return render(request,'login.html',{'name':filter[i].name})
                for i in range(n):
                    if (email != filter[i].email or usrName != filter[i].userName) and passBro != filter[i].passwd:
                        messages.success(request, 'No Data Found Please Sign up')
                        return render(request,'login.html')
    else:
        return render(request,'login.html')
>>>>>>> 2155350 (working now long signup contact)
=======
                        return render(request, 'login.html', {'name': filter[i].name})

                messages.success(request, 'No Data Found Please Sign up')
                return render(request, 'login.html')
    return render(request, 'login.html')


def home(request):
    datas = signp.objects.all()
    return render(request, 'home.html', {'info': datas})


def homes(request):
    datas = signp.objects.all()
    messages.success(request, 'Update Successfully! bro')
    return render(request, 'home.html', {'info': datas})


def deleteData(request, id):
    if request.method == 'POST':
        data = signp.objects.get(pk=id)
        print(data)
        data.delete()
        return HttpResponseRedirect('/home')


def update(request, id):
    if request.method == 'POST':
        data = signp.objects.get(pk=id)
        print(data)
        return render(request, 'update.html', {'info': data})
# def upda(request):


def updat(request, id):
        data = signp.objects.get(pk=id)
        if request.method == 'POST':
            data.name = request.POST.get('name', '')
            data.email = request.POST.get('email', '')
            data.userName = request.POST.get('Uname', '')
            data.passwd = request.POST.get('password', '')
            datas = {
                'name': data.name,
                'email': data.email,
                'userName': data.userName,
                'passwd': data.passwd,
            }
            print(datas)
            data.save()
            return HttpResponseRedirect('/homes')


def Personal(request):
    details = personal.objects.all()
    n = len(details)
   
   

    params={'detail':details,'deta':details,'detai':details}

    return render(request,'personal.html',params)

def gallary(request):
    return render(request,'gallary.html')

>>>>>>> 02329d5 (tatti gallary)



