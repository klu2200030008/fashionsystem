from django.urls import path
from .views import *

urlpatterns = [
    path("", myhome, name='home'),
    path("home1/", myhome1, name='home1'),
    path("about/", myabout, name='about'),
    path("about1/", myabout1, name='about1'),
    path("collections/", mycollections, name='collections'),
    path("refrences/", myrefrences, name='refrences'),
    path("shop/", myshop, name='shop'),
    path("feedback/", myfeedback, name='feedback'),
    path("feedback1/", myfeedback1, name='feedback1'),
    path("login/", mylogin,name='login'),
    path("registration/", myregistration,name='registration'),
    path("contact/", mycontact, name='contact'),
    path("login_view/contact1/", mycontact1, name='contact1'),
    path("login_view/", login_view, name='login_view'),
    path("registration_view/", registration_view, name='registration_view'),
    path('success/', success_page, name='success_page'),
    path('submit_feedback/', submit_feedback, name='submit_feedback'),
    path('login_view/home1.html', myhome, name='home_in_login'),
    path('login_view/about1.html', myabout, name='about_in_login'),
    path('login_view/shop.html', myshop, name='shop_in_login'),
    path('login_view/collections.html', mycollections, name='collections_in_login'),
    path('login_view/refrences.html', myrefrences, name='refrences_in_login'),
    path('home1/shop.html', myshop, name='shop_in_login'),
    path('home1/collections.html', mycollections, name='collections_in_login'),
    path('home1/refrences.html', myrefrences, name='refrences_in_login'),
    path('logout/', logout_view, name='logout'),



]
