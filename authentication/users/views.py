from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/index.html", {"message": "Please login!"})
    context = {
        "user": request.user
    }
    return render(request, "users/user.html", context)

def login_page(request):
    return render(request,"users/login.html")

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
        #here, goint back to index's url, index function will run, since logged in, it will take to user 
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials. Try again!"})

def signup_page(request):
    #return HttpResponseRedirect(reverse("signup_page"))
    return render(request, "users/signup.html")

def signup_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password1 = request.POST["pass1"]
        password2 = request.POST["pass2"]
        mail = request.POST["email"]
        if password1 == password2:
            form = UserCreationForm(request.POST)
            user = User.objects.create_user(username=username,
                                    email=mail,
                                    password=password1)
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/signup.html", {"message": "passwords not same!"})
        #return HttpResponseRedirect(reverse("index"))
        #return render(request, "users/user.html", context)
    else:
        return render(request, "users/index.html")

    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
    #return render(request, "users/index.html", {"message": "Logged out."})
