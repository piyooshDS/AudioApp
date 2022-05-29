""" docstring """
from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'aboutus', AboutUsAPI.as_view()),
    url(r'termsservices', TermsServicesAPI.as_view()),
    url(r'privacypolicy', PrivacyPolicyAPI.as_view()),
]
