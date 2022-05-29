""" docstring """
from rest_framework import serializers

from .models import *


class AboutUsSerializer(serializers.ModelSerializer):
    """ docstring """

    class Meta:
        """ docstring """
        model = AboutUs
        fields = "__all__"


class TermServicesSerializer(serializers.ModelSerializer):
    """ docstring """

    class Meta:
        """ docstring """
        model = TermServices
        fields = "__all__"


class PrivacyPolicySerializer(serializers.ModelSerializer):
    """ docstring """

    class Meta:
        """ docstring """
        model = PrivacyPolicy
        fields = "__all__"
