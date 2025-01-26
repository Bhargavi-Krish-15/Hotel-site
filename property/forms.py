from django import forms
from .models import Reserve


class ReserveForm(forms.ModelForm):

    class Meta:
        # model name for which we are creating the form for:
        model = Reserve
        # which are the fields we need to include in this model - all the fields in the model
        fields = "__all__"

# class PropertySearch(forms.ModelForm):
#     class Meta:
#         model = Property
#           fields = ['address', 'property_type']
