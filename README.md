# Giant_Leap
Django Project



<b>Prerequisities / Technical Details</b>

Django 2.2.3 or higher<br> 
Python 3.7<br>

<b>API Details</b>
```
https://api.nasa.gov/
```

<b> Installing </b>
<br>
You need to install Python 3.7. 
Django 2.2.

In Ubuntu, Mint and Debian you can install Python 3 like this:

```
$ sudo apt-get install python3 python3-pip
```

For other Linux flavors, macOS and Windows, packages are available at

http://www.python.org/getit/


You can find further information about Django

https://docs.djangoproject.com/en/2.2/topics/install/

<br>
<b> How to Start Project </b> 
<br>
 If you are using Linux Destro like Ubuntu, You need to replace pip and python to pip3 and python3
 
```
pip install
python manage.py migrate
python manage.py runserver
```


<br>
<b> Database Informations </b> 
<br>

Sqllite used.




<br>
<b> Admin Informations </b> 
<br>
 You can reach Admin panel from /admin.
 But before you need an account with admin permission, to create this; .

 
```
python manage.py createsuperuser
```

 <br>
 <b>IMPORTANT</b>

For development at nasa/settings.py -> DEBUG must be set to TRUE
<br>
(It left as true)
