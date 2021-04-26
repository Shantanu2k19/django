from django.urls import path

from . import views
#dot means current directory, imported view file

#this contain all the urls
urlpatterns = [
    path("",views.index)  #run index function from views for empty route
]