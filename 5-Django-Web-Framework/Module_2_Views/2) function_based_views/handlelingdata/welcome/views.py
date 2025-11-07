from django.shortcuts import render
from datetime import datetime

# Create your views here.


from django.http import HttpResponse    

def welcome(request):
    return HttpResponse("Welcome App")

def hello_anas(request):
    return HttpResponse("Hello, Anas!")

def current_time(request):
    date_joined = datetime.today().year
    return HttpResponse(f"Current time: {date_joined}")

def message(request):
    context = """
    <h1 style="color: red;">Hello, Deia!</h1>
    <p style="color: blue;">Welcome to the welcome app</p>
    """
    return HttpResponse(context)