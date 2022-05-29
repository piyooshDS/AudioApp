""" docstring"""
import jwt
from cloudinary.models import CloudinaryField as BaseCloudinaryField
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from rest_framework_jwt.utils import jwt_payload_handler


# from AudioApp.apps import get_model


# Create your models here.

class CloudinaryField(BaseCloudinaryField):
    """docstring for Companies"""

    def upload_options(self, model_instance):
        try:
            if model_instance.chapter:
                return {
                    'allowed_formats': ['mp3'],
                    'resource_type': 'raw',
                    'use_filename': True,
                }
        except:
            return {
                'allowed_formats': ['jpg,png'],
                'resource_type': 'raw',
                'use_filename': True,
            }


class Companies(models.Model):
    """docstring for Companies"""

    company_name = models.CharField(max_length=50, blank=True, null=True,
                                    error_messages={'invalid': 'max_length is 50.', 'required': ''})
    company_phone = models.CharField('Phone Number', max_length=20, blank=False, null=True, validators=[
        RegexValidator(regex='^[0-9_+]+$', message='Phone Number must be integer.')])
    logo = CloudinaryField(blank=True, null=True)
    street = models.CharField(max_length=50, error_messages={'invalid': 'max_length is 50.'})
    state = models.CharField(max_length=20, error_messages={'invalid': 'max_length is 50.'})
    country = models.CharField(max_length=20, error_messages={'invalid': 'max_length is 50.'})
    zipcode = models.IntegerField(blank=False,
                                  validators=[RegexValidator(regex='^[0-9_+]+$', message='Must be integer.')])
    representative_name = models.CharField(max_length=30, blank=True, null=True,
                                           error_messages={'invalid': 'max_length is 50.'})
    representative_email = models.EmailField(blank=False, null=False, unique=True)
    representative_phone = models.CharField(max_length=15, blank=True, null=True,
                                            validators=[
                                                RegexValidator(regex='^[0-9_+]+$',
                                                               message='Phone Number must be integer.')])
    is_subscribed = models.BooleanField('Subscribed', default=False)
    password = models.CharField(max_length=15, error_messages={'invalid': 'max_length is 50.'})
    created_at = models.DateTimeField('Date & Time', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

    class Meta:
        """docstring for meta"""
        verbose_name = "company"
        verbose_name_plural = "Company Management"


class MyUserManager(BaseUserManager):
    """
    Inherits BaseUserManager class
    """

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


# Base User Table used same for Authentication Purpose

class MyUser(AbstractBaseUser, PermissionsMixin):
    """docstring for MyUser"""

    email = models.EmailField('Email', max_length=60, blank=True, null=True, unique=True)
    is_staff = models.BooleanField(default=False)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, null=True, blank='True')
    is_active = models.BooleanField('Active', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    # Function for creating JWT for Authentication Purpose
    def create_jwt(self):
        """
        Function for creating JWT for Authentication Purpose
        """
        payload = jwt_payload_handler(self)
        token = jwt.encode(payload, settings.SECRET_KEY)
        auth_token = token.decode('unicode_escape')
        return auth_token

    def get_full_name(self):
        return str(self.email)

    def get_short_name(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        """docstring for meta"""
        verbose_name = "User"
        verbose_name_plural = "User Details"


class Employess(models.Model):
    """ docstring for Employees"""
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, default='')
    employee_id = models.IntegerField(unique=True)
    firstname = models.CharField(max_length=35, blank=True, null=True,
                                 error_messages={'max_length': 'Last name is too long.'}, validators=[
            RegexValidator(regex='^[A-Za-z]+$', message='Only alphabets are allowed.')])
    lastname = models.CharField(max_length=35, blank=True, null=True,
                                error_messages={'max_length': 'Last name is too long.'},
                                validators=[RegexValidator(regex='^[A-Za-z]+$', message='Only alphabets are allowed.')])
    image = CloudinaryField('image', blank=True, null=True)
    jobtitle = models.CharField(max_length=35, blank=True, null=True,
                                error_messages={'max_length': 'Job title is too long.'},
                                validators=[RegexValidator(regex='^[a-zA-Z_ ]+$', message='Only alphabets are allowed.')])
    employee_email = models.EmailField(blank=False, unique=True)
    date_time = models.DateField('Date', auto_now=False)
    employee_code = models.CharField(max_length=15, )
    is_employee = models.BooleanField('Is Employee?', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname

    class Meta:
        """docstring for meta"""
        verbose_name = "Employee"
        verbose_name_plural = "Employee Management"


class Lessons(models.Model):
    """ docstring"""
    lesson_name = models.CharField(max_length=30)
    lesson_admin_ID = models.CharField('Lesson ID ', max_length=6, blank=True, null=True)
    logo = CloudinaryField('logo', blank=True, null=True)
    # created_on = models.DateField('Date & Time', auto_now=False)
    percentage_status = models.FloatField('complete status', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ str function """
        return self.lesson_name

    class Meta:
        """docstring for meta"""
        verbose_name = "Lesson "
        verbose_name_plural = "Lesson Management"


class Chapters(models.Model):
    """docstring for Chapters"""
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    chapter_name = models.CharField('chapter name', max_length=20, blank=False)
    chapter = models.FileField('Add chapter')
    status = models.CharField(max_length=15, default='locked')
    is_complete = models.BooleanField('Is Complete?', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chapter_name

    class Meta:
        """docstring for meta"""
        verbose_name = "chapter"
        verbose_name_plural = "Chapters"


class CompanyLesson(models.Model):
    """docstring for assigning lesson to company"""
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, default='', related_name='companylesson')
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, default='', related_name='com')
    fee = models.BigIntegerField(default=0)
    Employee_slot = models.IntegerField(default=0)
    expiry_date = models.DateField(auto_now=False)
    created_at = models.DateTimeField('Purchase Date', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lesson)

    class Meta:
        """docstring for meta"""
        verbose_name = "Purchase History for"
        verbose_name_plural = "Purchase History"


class EmployeeLesson(models.Model):
    """docstring for assigning lesson to company"""
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, default='', related_name='employeelesson')
    employee = models.ForeignKey(Employess, on_delete=models.CASCADE, default='', related_name='lesson_employee')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_access = models.BooleanField(default=True)
    progress = models.CharField(max_length=15, default='incomplete')

    def __str__(self):
        return str(self.lesson)

    class Meta:
        verbose_name = "Employee Lesson Management"
        verbose_name_plural = "Assigned Lessons"
        unique_together = (('lesson', 'employee',),)


class ChapterEmployee(models.Model):
    """docstring for model class"""
    chapter=models.ForeignKey(Chapters,on_delete=models.CASCADE)
    employee=models.ForeignKey(Employess,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    is_complete = models.BooleanField('Is Complete?', default=True)

    def __str__(self):
        return str(self.employee)+str(self.chapter)


class Intro(models.Model):
    """ docstring for Intro class  """
    filename = models.CharField(max_length=15, blank=True)
    chapter = CloudinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.filename

    class Meta:
        """ Meta class Intro Model """
        verbose_name = "Upload Introduction"
        verbose_name_plural = "Upload Introduction"
