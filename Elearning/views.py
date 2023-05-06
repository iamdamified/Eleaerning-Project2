from django.shortcuts import render,redirect
from .models import *
# from django.contrib.auth.models import User
# from django.contrib import auth
from .forms import RegisterForm
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    # Unbound Instance
    if request.method == "GET":
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
        testimonial = Testimonial.objects.all()
        footcontact = Footcontact.objects.all()
        footgallery = Footgallerie.objects.all()

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
            'expert': expert,
            'testimonial': testimonial,
            'footcontact': footcontact,
            'footgallery': footgallery

        }
    # Bound instance
    elif request.method == "POST":
        #  validate
        # news_letter_instruction = request.POST["name"] # OR request.POST.get("name")
        new_subscribers_email = request.POST("email") # OR request.POST.get["email"]

         # The below is the ORM that describes what operation the application does with the data received from the user throught the form.
        Newsletter.objects.create(email=new_subscribers_email)


        # The below describes what the form reaction would be after submiting
        return HttpResponse("You have subscribed sucessfully")
        # return redirect("home")
    
# Learn more about SENDGRID on twilo.com to know how to distribute newsletters to emails collected from this form (twilo.com/blog/email-activation-django-sendgrid)


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


def registerpage(request):
    if  request.method == "POST": #CVS
        form = RegisterForm(request.POST)#collect
        if form.is_valid():#validate
            form.save()#save
            return HttpResponse("You have joined us and you will receive an email soon")
    

    else: 
        form = RegisterForm()

    context = {
        "form": form
    }


    return render(request, "Elearning/register.html", context)

    #"pip install django-crispy-forms" Type this in cmd to make forms better, and "crispy_forms"  and (CRISPY_TEMPLATE_PACK = "bootstrap4") in settings.py
# if it did not work go ahead to change crispy version pip install django-crispy-forms==1.14.0

def privacypage(request):
    return render(request, 'Elearning/privacy.html')


def termspage(request):
    return render(request, 'Elearning/terms.html')

def faqspage(request):
    return render(request, 'Elearning/faqs.html')


