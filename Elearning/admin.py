from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Carousel)
admin.site.register(Service)
admin.site.register(AboutImage)
admin.site.register(Feature)
admin.site.register(Categorie)
admin.site.register(Expert)
admin.site.register(Testimonial)
admin.site.register(Footcontact)
admin.site.register(Footgallerie)
admin.site.register(Newsletter)
admin.site.register(Register)




class CourseAdmin(admin.ModelAdmin):
    list_display = ["instructor", "name", "price"]
    
admin.site.register(Course, CourseAdmin)









