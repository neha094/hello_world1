from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return redirect('/')
