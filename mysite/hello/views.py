from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import menu
# Create your views here.
def index(request):
    #return HttpResponse("Hello World")

    #context dictionary to pass value
    context ={
        "temp": menu.objects.all()
    }
    return render(request, "hello/index.html",context)

def bill(request,num):
    try: 
        temp = menu.objects.get(pk=num)
    except menu.DoesNotExist:
        raise Http404("item does not exist")
    context = {
        "obj":temp
    }
    return render(request, "hello/item.html", context)