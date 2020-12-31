from django.contrib import admin

# Register your models here.
from .models import image_to_json

class image_to_jsonAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie_image', 'data']

admin.site.register(image_to_json, image_to_jsonAdmin)