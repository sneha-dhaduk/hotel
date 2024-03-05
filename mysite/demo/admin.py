from django.contrib import admin
from . import models


# Register your models here.
class CakeAdmin(admin.ModelAdmin):
    list_display=['title','contain','image','price']
admin.site.register(models.student)
admin.site.register(models.cake, CakeAdmin)
class carAdmin(admin.ModelAdmin):
   list_display=['name','color','price']
admin.site.register(models.car,carAdmin)
