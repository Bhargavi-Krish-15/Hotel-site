from django.shortcuts import render
from .models import About

# Create your views here.


def aboutus(request):
    about_us = About.objects.all
    template = "about/about.html"
    context = {
        "about_us": about_us
    }
    return render(request, template, context)
