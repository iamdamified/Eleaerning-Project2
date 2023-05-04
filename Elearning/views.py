from django.shortcuts import render
from .models import *

# Create your views here.

def homepage(request):
    carousel = Carousel.objects.all()
    service = Service.objects.all()
    aboutimage = AboutImage.objects.all()
    feature = Feature.objects.all()
    category1 = Categorie.objects.get(pk=1)
    category2 = Categorie.objects.get(pk=2)
    category3 = Categorie.objects.get(pk=3)
    category4 = Categorie.objects.get(pk=4)
    course = Course.objects.all()
    expert = Expert.objects.all()

    context = {
        'carousel': carousel,
        'service': service,
        'aboutimage': aboutimage,
        'feature': feature,
        'category1': category1,
        'category2': category2,
        'category3': category3,
        'category4': category4,
        'course': course,
        'expert': expert

    }
    return render(request, 'Elearning/index.html', context)

def contactpage(request):
    return render(request, 'Elearning/contact.html')

def coursespage(request):
    return render(request, 'Elearning/courses.html')

def teampage(request):
    return render(request, 'Elearning/team.html')

def testimonialpage(request):
    return render(request, 'Elearning/testimonial.html')

def aboutpage(request):
    return render(request, 'Elearning/about.html')

def Errorpage(request):
    return render(request, 'Elearning/404.html')

