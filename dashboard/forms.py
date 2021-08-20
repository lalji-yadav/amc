from django import forms
from .models import Amc
# from decimal import Decimal
from django.forms.widgets import NumberInput


class AmcForm(forms.ModelForm):
    CustomerName = forms.CharField(error_messages={'required': 'Please enter client name'},
                                   widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))

    AMC_TYPE = (
        ('', 'Select'),
        ('Quarterly', 'Quarterly'),
        ('Half yearly', 'Half yearly'),
        ('Annual', 'Annual'),
    )

    AmcType = forms.CharField(
        error_messages={'required': 'Please select AMC Type'},
        widget=forms.Select(choices=AMC_TYPE, attrs={'class': 'form-control form-control-sm'}),
    )

    AmcWarrenty = forms.CharField(error_messages={'required': 'Please enter Amc Warrenty'},
                                     widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))

    MaxFeeServices = forms.IntegerField(error_messages={'required': 'Please enter Max Fee Services'},
                                    widget=NumberInput(attrs={'class': 'form-control form-control-sm'}))

    StartDate = forms.DateField(error_messages={'required': 'Please enter Start Date'},
                                widget=NumberInput(attrs={'type': 'date', 'class' : 'form-control form-control-sm'}))

    EndDate = forms.DateField(error_messages={'required': 'Please enter End Date'},
                              widget=NumberInput(attrs={'type': 'date', 'class': 'form-control form-control-sm'}))

    email = forms.EmailField(error_messages={'required': 'Please enter valid Email'},
                             widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm',
                                                            'placeholder': 'email'}))

    class Meta:
        model = Amc
        fields = "__all__"

