
from django import forms
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField

# Copyright Videntity Systems Inc.


class PhoneVerifyCodeForm(forms.Form):
    code = forms.CharField(widget=forms.PasswordInput, max_length=30,
                           label=_('Code*'))
    required_css_class = 'required'


class PhoneForm(forms.Form):
    mobile_phone_number = PhoneNumberField(help_text=_("US numbers only."))
    verify_now = forms.BooleanField(required=False, initial=True)
