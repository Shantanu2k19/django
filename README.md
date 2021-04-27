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

