from django.contrib import admin
from .models import  NumerologyData

@admin.register(NumerologyData)
class  NumerologyDataAdmin(admin.ModelAdmin):
        list_display=['id','name','birthdate','website_link']
