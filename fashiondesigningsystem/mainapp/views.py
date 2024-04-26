from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib import auth
from django.contrib import messages
from .models import Feedback
from django.contrib.auth import logout
from django.shortcuts import redirect

from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib import messages
from .models import *
from .forms import FeedbackForm  # You'll need to create a form for your feedback model

from django.contrib.auth import logout
def myhome(request):
    return render(request, "home.html")
def myhome1(request):
    return render(request, "home1.html")
def myabout(request):
    return render(request, "about.html")
def myabout1(request):
    return render(request, "about1.html")
def mycollections(request):
    return render(request, "collections.html")
def myrefrences(request):
    return render(request, "refrences.html")
def myshop (request):
    return render(request, "shop.html")
def myfeedback(request):
    return render(request, "feedback.html")
def myfeedback1(request):
    return render(request, "feedback1.html")
def mycontact(request):
    return render(request, "contact.html")

def mycontact1(request):
    return render(request, "contact1.html")

def mylogin(request):
    return render(request, "login.html")

def myregistration(request):
     return render(request,"registration.html")

def success_page(request):
    return render(request, 'success.html')


def registration_view(request):
    user_exists = False
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        phone = request.POST['phone']
        if User.objects.filter(email=email).exists():
            messages.info(request, 'User with this email already exists. Please log in.')
            return render(request, 'login.html')
        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        user.save()
        messages.info(request, 'Account created Successfully!')
        return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)
        if user.check_password(password):
            # If username and password match, redirect to admin page
            if username== 'navya.vat071@gmail.com' and password == '123456':
                return render(request, 'index.html')
            else:
                return  render(request, 'home1.html')
        else:
            # If password does not match, display a message
            messages.info(request, 'Invalid password. Please try again')
            return render(request, 'login.html')


def logout_view(request):
  logout(request)  # Logs out the user
  return redirect('home')

def index(request):
    return render(request, 'index.html')

def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        rating = request.POST.get('rating')

        feedback = Feedback(name=name, email=email, message=message, rating=rating)
        feedback.save()

        messages.success(request, 'Feedback submitted successfully!')
        return redirect('submit_feedback')

    return render(request, 'feedback_form.html')



