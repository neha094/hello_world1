from django.contrib.auth.models import User
from django.shortcuts import render,redirect

# Create your views here.
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        firstname =request.POST['firstname']
        lastname = request.POST['lastname']
        emailid = request.POST['emailid']
        password= request.POST['password']

        x=User .objects.create_user(username=username,first_name=firstname,last_name=lastname,email=emailid,password=password)
        x.save()
        print('user created')
        return redirect('/')


    return render(request,'b.html')
