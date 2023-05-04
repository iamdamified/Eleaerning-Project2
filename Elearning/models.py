from django.db import models

# Create your models here.

class Carousel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    explanation = models.TextField()
    image = models.ImageField(upload_to="carousel_images")

    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class AboutImage(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='about_image')

    def __str__(self):
        return self.name
    
class Feature(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Categorie(models.Model):
    name = models.CharField(max_length=50)
    courses_count = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_image')
    
    
    def __str__(self):
        return self.name
    
    
class Course(models.Model):
    image = models.ImageField(upload_to='course_image')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    likes_count = models.IntegerField()
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    duration = models.DecimalField(max_digits=10, decimal_places=2)
    student_count = models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
class Expert(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    image = models.ImageField(upload_to='expert_image')
    
    
    def __str__(self):
        return self.name