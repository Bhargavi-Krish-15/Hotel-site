from django.urls import path
from . import views

app_name = "property"

urlpatterns = [
    path('', views.property_list, name="property_list"),
    # so we get the list of objects from the views.py , but object we want is based on the id , hence we pass in the url
    #inorder to link the view , we use the name that we gave here property_detail to link to other views with %url%
    path('<int:id>', views.property_detail, name="property_detail"),
]
