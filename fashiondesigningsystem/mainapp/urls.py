from django.urls import path
from .views import *

urlpatterns = [
    path("", myhome, name='home'),
    path("home1/", myhome1, name='home1'),
    path("about/", myabout, name='about'),
    path("about1/", myabout1, name='about1'),
    path("kidswear/", mykidswear, name='kidswear'),
    path("ladieswear/", myladieswear, name='ladieswear'),
    path("feedback/", myfeedback, name='feedback'),
    path("feedback1/", myfeedback1, name='feedback1'),
    path("login/", mylogin,name='login'),
    path("cart/", mycart,name='cart'),
    path("index/", myindex,name='index'),
    path("menswear/", mymenswear,name='menswear'),
    path("registration/", myregistration,name='registration'),
    path("contact/", mycontact, name='contact'),
    path("login_view/contact1/", mycontact1, name='contact1'),
    path("login_view/", login_view, name='login_view'),
    path("registration_view/", registration_view, name='registration_view'),
    path('login_view/home1.html', myhome, name='home_in_login'),
    path('login_view/about1.html', myabout, name='about_in_login'),
    path('login_view/ladieswear.html', myladieswear, name='ladieswear_in_login'),
    path('login_view/kidswear.html', mykidswear, name='kidswear_in_login'),
    path('login_view/menswear.html', mymenswear, name='menswear_in_login'),
    path('home1/menswear.html', mymenswear, name='menswear_in_login'),
    path('home1/ladieswear.html', myladieswear, name='ladieswear_in_login'),
    path('home1/kidswear.html', mykidswear, name='kidswear_in_login'),
    path('home1/cart.html', mycart, name='cart_in_login'),
    path('logout/', logout_view, name='logout'),


]
