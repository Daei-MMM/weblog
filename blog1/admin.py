from django.contrib import admin
from .models import post , todo

# Register your models here.

admin.site.register(todo)
admin.site.register(post)