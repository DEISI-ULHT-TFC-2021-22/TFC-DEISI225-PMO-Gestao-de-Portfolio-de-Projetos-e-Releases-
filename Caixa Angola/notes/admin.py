from django.contrib import admin

# Register your models here.
from .models import MyNote

admin.site.register(MyNote)