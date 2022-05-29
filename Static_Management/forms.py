from django import forms
from djrichtextfield.widgets import RichTextWidget

from .models import *


class AboutUsModelAdmin(forms.ModelForm):
    """ docstring """
    content = forms.CharField(widget=RichTextWidget(attrs={'rows': 10, 'cols': 100}))

    class Meta:
        """ docstring """
        model = AboutUs
        fields = ["heading", "content", "company"]


class TermsServicesModelAdmin(forms.ModelForm):
    """ docstring """
    content = forms.CharField(widget=RichTextWidget(attrs={'rows': 10, 'cols': 100}))

    class Meta:
        """ docstring """
        model = TermServices
        fields = ["heading", "content", "company"]


class PrivacyPolicyModelAdmin(forms.ModelForm):
    """ docstring """
    content = forms.CharField(widget=RichTextWidget(attrs={'rows': 10, 'cols': 100}))

    class Meta:
        """ docstring """
        model = PrivacyPolicy
        fields = ["heading", "content", "company"]
