from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login_helper", views.login_page, name="login_page"),
    path("login", views.login_view, name="login"),

    path("signup_helper", views.signup_page, name="signup_page"),
    path("signup", views.signup_view, name="signup"),
    
    path("logout", views.logout_view, name="logout")
]
