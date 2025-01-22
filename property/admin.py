from django.contrib import admin

# Register your models here.

# we have to register all the models that we define in our models.py so that this can be visible from the admin view.

from .models import Property, Category

admin.site.register(Property)
admin.site.register(Category)
