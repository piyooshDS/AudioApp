""" file for forms"""
from django import forms

from .models import Companies, Employess, MyUser, Lessons, Chapters, Intro


class CompanySignUp(forms.ModelForm):
    """ CompanySignUp form  """
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_logo(self):
        cleaned_data = super(CompanySignUp, self).clean()
        file = cleaned_data.get('logo')
        if file:
            try:
                if file.format == "jpg" or file.format == ".png" or file.format == ".jpeg":
                    return file
            except:
                filename = file.name
                if not (filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png')):
                    raise forms.ValidationError("Invalid File Type")
                return file

    def clean_zipcode(self):
        cleaned_data = super(CompanySignUp, self).clean()
        zipcode = cleaned_data.get('zipcode')
        if len(str(zipcode)) != 6:
            raise forms.ValidationError("Only 6 digits are allowed.")
        return zipcode

    def clean_representative_email(self):
        cleaned_data = super(CompanySignUp, self).clean()
        representative_email = cleaned_data.get('representative_email')
        if len(str(representative_email)) > 50:
            raise forms.ValidationError("Max 50 characters are allowed.")
        return representative_email

    def save(self, commit=True):
        company = super(CompanySignUp, self).save(commit=False)
        email = self.cleaned_data.get("representative_email")
        password = self.cleaned_data.get("password")
        user, created = MyUser.objects.update_or_create(email=email)
        user.company=self.cleaned_data.get("company")
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.save()
        company.save()
        return company

    class Meta:
        """ doctstring for meta class"""
        model = Companies
        fields = "__all__"


class EmployeeSignUp(forms.ModelForm):

    def clean_employee_code(self):
        cleaned_data = super(EmployeeSignUp, self).clean()
        employee_code = cleaned_data.get('employee_code')
        if " " in employee_code:
            raise forms.ValidationError("Whitespaces are not allowed.")
        elif len(employee_code) < 8 or len(employee_code) > 16:
            raise forms.ValidationError("Employee code length must be between 8 to 16.")
        return employee_code

    def clean_image(self):
        cleaned_data = super(EmployeeSignUp, self).clean()
        file = cleaned_data.get('image')
        if file:
            try:
                if file.format == "jpg" or file.format == ".png" or file.format == ".jpeg":
                    return file
            except:
                filename = file.name
                if not (filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png')):
                    raise forms.ValidationError("Invalid File Type")
                return file
        return file

    def save(self, commit=True):
        print("employee signup")
        employee = super(EmployeeSignUp, self).save(commit=False)
        email = self.cleaned_data.get("employee_email")
        password = self.cleaned_data.get("employee_code")
        user, created = MyUser.objects.update_or_create(email=email)
        user.set_password(password)
        user.company=self.cleaned_data.get("company")
        user.is_active = True
        user.save()
        employee.save()
        return employee

    class Meta:
        """ docstring for class meta """
        model = Employess
        fields = "__all__"


class LessonsSignUp(forms.ModelForm):
    """ Lesson SigUp from"""

    def clean_logo(self):
        cleaned_data = super(LessonsSignUp, self).clean()
        file = cleaned_data.get('logo')
        if file:
            try:
                if file.format == "jpg" or file.format == ".png" or file.format == ".jpeg":
                    return file
            except:
                filename = file.name
                if not (filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png')):
                    raise forms.ValidationError("Invalid File Type")
                return file

    class Meta:
        model = Lessons
        fields = "__all__"


class ChapterAdd(forms.ModelForm):
    """ form for chapter """

    def clean_chapter(self):
        cleaned_data = super(ChapterAdd, self).clean()
        file = cleaned_data.get('chapter')
        if file:
            try:
                if file.format == ".mp3" or file.format == ".ogg" or file.format == ".wav":
                    return file
            except:
                filename = file.name
                if not (filename.endswith('.mp3') or filename.endswith('.ogg') or filename.endswith('.wav')):
                    raise forms.ValidationError("Invalid File Type")
                return file
        else:
            raise forms.ValidationError("Please select a audio File.")

    class Meta:

        model = Chapters
        fields = "__all__"


class Purchaseform(forms.ModelForm):
    """ form for Purchase from """

    def save(self, commit=True):
        Purchase = super(Purchaseform, self).save(commit=False)
        Purchase.company.is_subscribed = True
        Purchase.company.save()
        Purchase.save()
        return Purchase


class Introform(forms.ModelForm):
    """ docstring for Intro admin form """

    def clean_chapter(self):
        cleaned_data = super(Introform, self).clean()
        file = cleaned_data.get('chapter')
        if file:
            try:
                if file.format == ".mp3" or file.format == ".ogg" or file.format == ".wav":
                    return file
            except:
                filename = file.name
                if not (filename.endswith('.mp3') or filename.endswith('.ogg') or filename.endswith('.wav')):
                    raise forms.ValidationError("Invalid File Type")
                return file
        else:
            raise forms.ValidationError("Please select a audio File.")
        return file

    class Meta:

        model = Intro
        fields = "__all__"
