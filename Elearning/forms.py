from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Register


# class UserReguistrationForm(UserCreationForm):
#     email = forms.EmailField(help_text="Please enter a valid email address")
#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]

COURSE_CHOICES = (
        ("BD", "Backend with Django"),
        ("FD", "Frontend Design"),
        ("PD", "Product Design")
    )

COHORT_CHOICES = (
        ("BY", "Beginning of Year"),
        ("MY", "Mid of Year"),
        ("EY", "End of Year")
    )



class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ["name", "email", "course", "cohort", "message"] #OR fields = "__all__"