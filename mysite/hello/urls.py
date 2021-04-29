from django.urls import path

from . import views
#dot means current directory, imported view file

#this contain all the urls
urlpatterns = [
    path("",views.index,name="homePage"),  #run index function from views for empty route
    path("<int:num>",views.itemInfo,name="itemPage"),

    path('login', views.handLogin, name="login"),
    path("register/",views.handleSignUp, name="register"),
    path("verified/",views.verified, name="verified"),
]
#naming route to refer it easily