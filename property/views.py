from django.shortcuts import render , redirect
from .models import Property, Category
from .forms import ReserveForm
from django.db.models import Q

# Create your views here.


def property_list(request):
    # we can define our object so that it can be passed to our views file - the template
    # next is which file should we redirect
    # and what and how do we pass that content.
    property_list = Property.objects.all()
    template = "property/list.html"

    rooms_search_keyword = request.GET.get('search_bar', '')
    property_type = request.GET.get('property_type', '')
    #filtering
    if rooms_search_keyword or property_type:
 
        property_list = property_list.filter(
            Q(name__icontains=rooms_search_keyword) &
            Q(property_type=property_type)
        )

    context = {
        "property_list": property_list
    }

    return render(request, template, context)


def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    # print("-----", property_detail.area)
    template = "property/detail.html"

    # the request that we recieve from our url is post
    # we called post method in the form. hence we recieve the details and save it.
    if request.method == "POST":
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
            return redirect('property:property_detail', id=id)
    else:
        reserve_form = ReserveForm()

    context = {
        "property_detail": property_detail,
        "reserve_form": reserve_form
    }

    return render(request, template, context)
