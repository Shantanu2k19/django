# django
uploading previous and new Django projects 

#python manage.py runserver
django-admin startproject name

python manage.py startapp app_name

app- urls.py : edit
app- create views.py, add views 

project's - urls.py : add path for apps

last configuration step:
    add your app in settings.py of mysite in installed apps. 
    'hello.apps.HelloConfig',
                    from apps.py


app - Models.py 
    create database, tables here 

python manage.py makemigrations
#detect changes in models.py 

#for the sql code of the migration :
python manage.py sqlmigrate flights 0001

#apply migrations 
python manage.py migrate

#django shell
pyhton manage.py shell



from hello.models import menu

f = menu(item="samosa", code="sam", price="10")

f.save()

#__str__ function added in models.py for ouput in proper form when printed 

menu.objects.all()
#querry all objects 

f = menu.objects.first()

f.delete()



#putting customers
from hello.models import customers
f = menu.objects.first()
c = customer(name="shan", order=f, bill=15)
c.save()

c.name   //shan
c.order.item //samosa

f.cu_orders.all() //<menu:  samosa, code: sam costing 10Rs. >



for html pages 
create 
folder templates
folder hello(app name inside it)
then index.html inside it
add route in views.py


#add and modify data using admin
register menu and customer in admin.py


create user account for admin
python manage.py createsuperuser
name : zodiac
email : 2030
password : shan@2001
pass - shan@2002 -- for authentication app



1. add a url in apps urls.py and direct to a function
2. write that function in views.py and render html page passing context
3. make html page in templates


#creating a user in shell 
from django.contrib.auth.models import User
user = Users.objects.create_user("username","abc@smth.com","password")
user.first_name="shan"
user.save()

shan
pass : 12345

