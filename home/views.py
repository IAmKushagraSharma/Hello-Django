from django.shortcuts import render, HttpResponse
from datetime import datetime  
from home.models import Contact
from django.contrib import messages


def index(request):
    # return HttpResponse("<b>This is index</b>")
    # messages.success(request, "this is a test message")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        desc = request.POST.get('desc')
        contact = Contact(fname=fname, lname=lname, email=email, phone=phone, city=city, state=state, pincode=pincode, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your form has been submited!!')
    return render(request, 'contact.html')

