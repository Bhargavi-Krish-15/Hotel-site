"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace="home")),
    path('property/', include('property.urls', namespace="property")),
    path('agents/', include('agents.urls', namespace="agents")),
    path('aboutus/', include('about.urls', namespace="about")),
    path('contact/', include('contact.urls', namespace="contact")),
]

# when we wanna add media files, images to the pages we add these in url to include it and check fo rthe correct settings
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = " HOTEL RESERVATION ADMIN"
admin.site.site_title = " HOTEL RESERVATION ADMIN"
admin.site.site_index_title = " Welcome To Hotel Reservation Admin"