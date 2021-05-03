from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages 

from django.views.decorators.csrf import ensure_csrf_cookie

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 

from .models import menu
# Create your views here.



def index(request):
    #context dictionary to pass value
    context ={
        "temp": menu.objects.all()
        #"SNAX":menu.objects.all().filter(category="snax"),
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
                "temp" : menu.objects.all()
            }
            return redirect("verified")
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
        return redirect("verified")
        #return render(request, "hello/verified.html",context)
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

def billing(request):
    if request.method == 'POST':
        ####   BILLING  #####
        MENU = menu.objects.all()
        bill = 0
        info2={}
        
        for item in MENU:
            #whether item selected
            temp = request.POST.get('ord'+item.code, 0)
            #if Yes
            if temp == "1":  
                listt = []
                temp2 = request.POST.get('quan'+item.code, 0)
                temp2 = int(temp2)+0  
                bill += item.price*temp2

                key_=str(item.item)
                listt.append(key_)
                listt.append(item.price)
                listt.append(temp2)
                listt.append(temp2*item.price)
                info2[key_]=listt
        print(info2)
    context = {
        "bill":bill,
        "temp": menu.objects.all(),
        "info2":info2
    }
    return render(request, "hello/checkout.html",context)
    #return rendirect("checkout")