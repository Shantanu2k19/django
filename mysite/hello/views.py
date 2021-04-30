from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages 


from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 

from .models import menu
# Create your views here.


def index(request):
    #context dictionary to pass value
    context ={
        "temp": menu.objects.all()
    }
    return render(request, "hello/index.html",context)


def handLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            context ={
                "temp": menu.objects.all()
            }
            return render(request, "hello/verified.html",context)
            #return HttpResponseRedirect(reverse(""))
            #return redirect("verified")
        else:
            messages.info(request, 'Invalid credentials. Please try again!')
            return redirect("index")

    return HttpResponse("404- Not found")
    return HttpResponse("login")

def handlogout(request):
    logout(request)
    context ={
        "temp": menu.objects.all()
    }
    messages.info(request, 'Logged out!')
    #return render(request, "hello/index.html",context)
    return HttpResponseRedirect(reverse("index"))

def signup_page(request):
    return render(request, "hello/signup.html")

def signup_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["pass1"]
        mail = request.POST["email"]
        form = UserCreationForm(request.POST)
        user = User.objects.create_user(username=username,
                                    email=mail,
                                    password=password)
        login(request, user)
        context ={
                "temp": menu.objects.all()
            }
        return render(request, "hello/verified.html",context)
        #return HttpResponseRedirect(reverse("index"))
        #return render(request, "users/user.html", context)
    else:
        return render(request, "hello/index.html")

def itemInfo(request,num):
    try: 
        temp = menu.objects.get(pk=num)
    except menu.DoesNotExist:
        raise Http404("item does not exist")
    context = {
        "obj":temp
    }
    return render(request, "hello/item.html", context)

def verified(request):
    context ={
        "temp": menu.objects.all()
    }
    return render(request, "hello/verified.html",context)