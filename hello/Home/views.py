from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

def index(request):
    context = {
        'variable' : 'priyanshu is great'
    }
    return render(request,'index.html',context)
    #return HttpResponse('This is a homepage!')

def about(request):
    #return HttpResponse('This is a ABOUT page!')
    return render(request,'about.html')

def icecreams(request):
    #return HttpResponse('This is a SERVICE page!')
    return render(request,'icecreams.html')

def softies(request):
    #return HttpResponse('This is a SERVICE page!')
    return render(request,'softies.html')

def IcecreamCakes(request):
    #return HttpResponse('This is a SERVICE page!')
    return render(request,'IcecreamCakes.html')

def contact(request):
    #return HttpResponse('This is a Contact page!')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your messages has been sent!")
    return render(request,'contact.html')