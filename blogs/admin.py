from django.contrib import admin
from .models import BlogPost # the dot in front of models tells Django to look for models.py in the same directory as admin.py


admin.site.register(BlogPost) # tells Django to manage our model through the admin site


