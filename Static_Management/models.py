""" docstring """
from django.db import models

from AudioApp.models import Companies


# Create your models here.


# table for AboutUs
class AboutUs(models.Model):
    """ docstring """
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, default=1)
    heading = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField()

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.heading


# table for terms and Conditions
class TermServices(models.Model):
    """ docstring """
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, default=1)
    heading = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField()

    class Meta:
        """docstring for meta"""
        verbose_name_plural = " Terms & Services"

    def __str__(self):
        return self.heading


# table for Privacy-policies
class PrivacyPolicy(models.Model):
    """ docstring """
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, default=1)
    heading = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField()

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Privacy Policy"

    def __str__(self):
        return self.heading
