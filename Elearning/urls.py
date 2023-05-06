from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage, name='home'),
    path('register/', registerpage, name='register'),
    path('contact/', contactpage, name='contact'),
    path('courses/', coursespage, name='courses'),
    path('team/', teampage, name='team'),
    path('testimonial/', testimonialpage, name='testimonial'),
    path('about/', aboutpage, name='about'),
    path('404/', Errorpage, name='404'),
    path('privacy/', registerpage, name='privacy'),
    path('terms/', termspage, name='terms'),
    path('faqs/', faqspage, name='faqs')


]