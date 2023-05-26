from django.contrib import admin
from .models import Profile #why using dot before the name


admin.site.register(Profile)
