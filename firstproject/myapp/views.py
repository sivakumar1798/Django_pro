from django.http.response import HttpResponse
from django.shortcuts import render
from myapp.models import MyappStudent
from django.db import models
from django.contrib import messages

# Create your views here.
def myview(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def Insertrecord(request):
    if request.method=="POST":
        saverecord= MyappStudent(user_name=request.POST['name'], mail_id=request.POST['Email'],
        phone_number=request.POST['phone'],address=request.POST['address'],password=request.POST['pws'],
        confirm_password=request.POST['confirmpws'])
        saverecord.save()
        print(saverecord)
        messages.success(request,'Record saved succesfully.....!')
        return render(request,'signup.html')
    

def show(request):
    a=MyappStudent.objects.get(user_name="SIVA")
    print(a.user_name)
    return HttpResponse("success")





