from django.urls import path

from . import views
#dot means current directory, imported view file

#this contain all the urls
urlpatterns = [
    path("",views.index,name="index"),  
    path('login', views.handLogin, name="login"),
    path('logout',views.handlogout,name="logout"),
    path("signup_helper",views.signup_page, name="signup_page"),
    path("signup", views.signup_view, name="signup"),

    path("<int:num>",views.itemInfo,name="itemPage"),
    path("verified",views.verified, name="verified"),
]
#naming route to refer it easily