from datetime import datetime
from django.shortcuts import render, redirect
from origin.models import contact_data
import pywhatkit as what
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        ph=request.POST.get('phone')
        email=request.POST.get('email')
        msg=request.POST.get('message')
        obj=contact_data(name=name,phone=ph,email=email,msg=msg)
        obj.save()
        messages.success(request,"Thank you for contacting us...")
        return redirect('index')
    else:
        return render(request, 'contact.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def whatsapp(request):
    if request.method == 'POST':
        msg = request.POST.get('msg')
        obj_now = datetime.now()
        hour=obj_now.hour
        print(hour)
        min=obj_now.minute+1
        print(min)
        what.sendwhatmsg('+91123456789', msg,hour,min)
        return redirect('index')
    else:
        return render(request, 'whatsapp.html')

def responseList(request):
    obj=contact_data.objects.all()
    return render(request,'responseList.html',{'list':obj})

def deleteData(request):
    if request.method=='POST':
        id=request.POST.get('id')
        obj=contact_data.objects.get(id=id)
        obj.delete()
        messages.success(request,'Deleted Successfully.')
        return redirect('responseList')


def sort(request):
    if request.method=='POST':
        value=request.POST.get('value')
        obj=contact_data.objects.order_by(value)
        return render(request,'responseList.html',{'list':obj})


def search(request):
    if request.method=='POST':
        value=request.POST.get('search')
        if contact_data.objects.filter(name=value).exists():
            obj=contact_data.objects.filter(name=value)
        elif contact_data.objects.filter(email=value).exists():
            obj=contact_data.objects.filter(email=value)
        else:
            obj=contact_data.objects.filter(phone=value)
        return render(request,'responseList.html',{'list':obj})