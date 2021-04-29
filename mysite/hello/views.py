from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages 


from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 

from .models import menu
# Create your views here.
def index(request):
    #return HttpResponse("Hello World")

    #context dictionary to pass value
    context ={
        "temp": menu.objects.all()
    }
    return render(request, "hello/index.html",context)

def itemInfo(request,num):
    try: 
        temp = menu.objects.get(pk=num)
    except menu.DoesNotExist:
        raise Http404("item does not exist")
    context = {
        "obj":temp
    }
    return render(request, "hello/item.html", context)

def registerPage(request):
    #form = UserCreationForms()
    #context={}
    return render(request, "hello/register.html")

def loginPage(request):
    return render(request, "hello/login.html")


def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
       # messages.success(request, " Your iCoder has been successfully created")
        return render(request, "hello/verified.html")
    else:
        return HttpResponseRedirect("homePage")

def handLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            #return HttpResponseRedirect(reverse("homePage"),mssg)
            #return render(request, "hello/verified.html", {"message": "Logged out."})
            return redirect("verified")
        else:
            return redirect("homePage")

    return HttpResponse("404- Not found")
    return HttpResponse("login")


def verified(request):
    context ={
        "temp": menu.objects.all()
    }
    return render(request, "hello/verified.html",context)
    #return render(request, "hello/verified.html", {"message": "Logged out."})
