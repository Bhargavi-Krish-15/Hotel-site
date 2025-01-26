from django.shortcuts import render, redirect
from .models import ContactDetails

# Create your views here.
from .forms import ContactForm
from django.core.mail import send_mail as sm, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# contact details model will have our owener's detail. so in order for people to contact to us through mail, we are making a mail form
# so this form will allow user to send mail to us. and we are inserting that form in html file
# instead of doing a direct html fform, we are going in django way. hence we create a python form file and include our form contents attributes there.
# we will call that form in the ui.
# teh below method is the logic for what do after getting that data from the fields


def send_mail(request):
    contact_details = ContactDetails.objects.last()

    # form actions
    contact_form = 'contact/contact.html'
    # post means any submission
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # extracts the user input
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']

            # with that input it trys to send email
            try:
                sm(subject, message, from_email, ['test@gmail.com'])
            except BadHeaderError:
                return HttpResponse('invalid header')
            # if its a successfull, we are calling the success method
            return redirect('contact:success')
    # orelse it renders a new empty form
    else:
        contact_form = ContactForm()

    template = "contact/contact.html"
    context = {
        "contact_details": contact_details,
        "contact_form": contact_form
    }

    return render(request, template, context)


def success(request):
    return HttpResponse('Message Sent successfully!!')
