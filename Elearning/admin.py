from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Carousel)
admin.site.register(Service)
admin.site.register(AboutImage)
admin.site.register(Feature)
admin.site.register(Categorie)
admin.site.register(Expert)


class CourseAdmin(admin.ModelAdmin):
    list_display = ["instructor", "name", "price"]
    
admin.site.register(Course, CourseAdmin)









