from django.shortcuts import render
from django.http import HttpResponse

from .models import menu
# Create your views here.
def index(request):
    #return HttpResponse("Hello World")

    #context dictionary to pass value
    context ={
        "temp": menu.objects.all()
    }
    return render(request, "hello/index.html",context)