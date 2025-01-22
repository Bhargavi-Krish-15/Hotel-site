from django.shortcuts import render
from .models import Property, Category

# Create your views here.


def property_list(request):
    #we can define our object so that it can be passed to our views file - the template
    #next is which file should we redirect
    #and what and how do we pass that content.
    properties_list = Property.objects.all
    template = "property/list.html"
    context = {
        "properties_list": properties_list
    }

    return render(request, template, context)


def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    # print("-----", property_detail.area)
    template = "property/detail.html"
    context = {
        "property_detail": property_detail
    }

    return render(request, template, context)
