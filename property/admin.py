from django.contrib import admin

# Register your models here.

# we have to register all the models that we define in our models.py so that this can be visible from the admin view.

from .models import Property, Category, Reserve


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'property_type', 'category',
                    'area', 'bed_count', 'bath_count', 'garage_count']
    search_fields = ['name', 'property_type']
    list_filter = ['category', 'property_type']


admin.site.register(Property, PropertyAdmin)
admin.site.register(Category)
admin.site.register(Reserve)
