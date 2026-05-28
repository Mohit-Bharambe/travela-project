
from django.urls import path
from .views import *

urlpatterns = [
 
    path('',index,name='index'),
    path('about/' ,about,name='about'),
    path('blog/' ,blog,name='blog'),
    path('booking/' ,booking,name='booking'),
    path('contact/' ,contact,name='contact'),
    path('destination/' ,destination,name='destination'),
    path('error/' ,error,name='error'),
    path('gallery/' ,gallery,name='gallery'),
    path('guides/' ,guides,name='guides'),
    path('packages/' ,packages,name='packages'),
    path('services/' ,services,name='services'),
    path('testimonial/' ,testimonial,name='testimonial'),
    path('tour/' ,tour,name='tour'),
    path('login/' ,login,name='login'),
    path('register/' ,register,name='register'),
    path('logout/' ,logout,name='logout'),
]
