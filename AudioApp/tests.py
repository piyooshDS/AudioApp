""" file for test"""
from datetime import date
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
import AudioApp.models
from GenericValidator.AlphaCheckValidation import AlphaCheckValidation
from GenericValidator.AlphaNumericCheckValidation import AlphaNumericCheckValidation
from GenericValidator.ConfirmPasswordValidator import ConfirmPasswordValidaton, AddressValidation
from GenericValidator.MaximumDateValdiatior import MaximumDateValdiation
from GenericValidator.MinimumDateValdiatior import MinimumDateValdiation
from GenericValidator.emailValidator import EmailValidation
from GenericValidator.firstNameValidator import FirstNameValidation
from GenericValidator.inArrayContains import InArrayContainsValidation
from GenericValidator.lastNameValidator import LastNameValidation
from GenericValidator.mobileValidator import MobileValidation
from GenericValidator.numberValidator import NumberValidation
from GenericValidator.passwordValidator import PasswordValidation
from GenericValidator.zipCodeValidator import ZipCodeValidation


class TestCaseClass(TestCase):
    """docstring for TestCaseClass"""

    def test_email(self):
        self.__email = "imtiyaz.ahemad@mobiloittegroup.com"
        emailObj = EmailValidation(self.__email, 10, 40)
        self.assertEqual(True, emailObj.validation())

    def test_req_email(self):
        self.__email = "imtiyaz.ahemad@mobiloittegroup.com"
        emailObj = EmailValidation(self.__email, 10, 40)
        self.assertEqual(True, emailObj.req_validation())

    def test_max_email(self):
        self.__email = "imtiyaz.ahemad@mobiloittegroup.com"
        emailObj = EmailValidation(self.__email, 10, 40)
        self.assertEqual(True, emailObj.max_validation())

    def test_min_email(self):
        self.__email = "imtiyaz.ahemad@mobiloittegroup.com"
        emailObj = EmailValidation(self.__email, 10, 40)
        self.assertEqual(True, emailObj.min_validation())

    def test_alphanumeric_mail(self):
        self.__email = "piyoosh99352gmail.com"
        Obj = EmailValidation(self.__email, 10, 40)
        self.assertEqual(True, Obj.alpha_numeric())

    def test_alpha_mail(self):
        self.__email = "PIY@GAMIL.com"
        emailObj = EmailValidation(self.__email, 10, 40)
        self.assertEqual(True, emailObj.alpha_validation())

    def test_lefttrim_mail(self):
        self.__email = "piyoosh9935@gmail.com"
        emailObj = EmailValidation(self.__email, 10, 40)
        self.assertEqual(True, emailObj.left_trim_validation())

    def test_firstName(self):
        self.__firstName = "Imtiyaz"
        firstNameObj = FirstNameValidation(self.__firstName, 2, 2)
        self.assertEqual(True, firstNameObj.req_validation())

    def test_min_firstName(self):
        self.__firstName = "Imtiyaz"
        firstNameObj = FirstNameValidation(self.__firstName, 2, 20)
        self.assertEqual(True, firstNameObj.min_validation())

    def test_max_firstName(self):
        self.__firstName = "Imtiyaz"
        firstNameObj = FirstNameValidation(self.__firstName, 2, 20)
        self.assertEqual(True, firstNameObj.max_validation())

    def test_req_firstName(self):
        self.__firstName = "dsfdsf"
        firstNameObj = FirstNameValidation(self.__firstName, 2, 20)
        self.assertEqual(True, firstNameObj.req_validation())

    def test_alphanumeric_firstname(self):
        self.__firstName = "piyoosh9935"
        firstNameObj = FirstNameValidation(self.__firstName, 2, 20)
        self.assertEqual(True, firstNameObj.alpha_numeric())

    def test_alpha_firstname(self):
        self.__firstName = "PIY"
        firstNameObj = FirstNameValidation(self.__firstName, 2, 20)
        self.assertEqual(True, firstNameObj.alpha_validation())

    def test_lefttrim_firstname(self):
        self.__firstName = "Imtiyaz"
        firstNameObj = FirstNameValidation(self.__firstName, 2, 20)
        self.assertEqual(True, firstNameObj.left_trim_validation())

        self.__array = [1, 2, 3, 4, 5, 56, 67, 78, 9]
        self.__Value = 67
        inArrayObj = InArrayContainsValidation(self.__array, self.__Value)
        self.assertEqual(True, inArrayObj.validation())

    #####

    def test_lastName(self):
        self.__lastName = "Khan"
        lastNameObj = LastNameValidation(self.__lastName, 2, 10)
        self.assertEqual(True, lastNameObj.validation())

    def test_req_lastName(self):
        self.__lastName = "Khan"
        lastNameObj = LastNameValidation(self.__lastName, 2, 10)
        self.assertEqual(True, lastNameObj.req_validation())

    def test_min_lastName(self):
        self.__lastName = "Khan"
        lastNameObj = LastNameValidation(self.__lastName, 2, 10)
        self.assertEqual(True, lastNameObj.min_validation())

    def test_max_lastName(self):
        self.__lastName = "Khan"
        lastNameObj = LastNameValidation(self.__lastName, 2, 10)
        self.assertEqual(True, lastNameObj.max_validation())

    def test_alphanumeric_lastName(self):
        self.__lastName = "piyoosh9935"
        lastNameObj = LastNameValidation(self.__lastName, 2, 20)
        self.assertEqual(True, lastNameObj.alpha_numeric())

    def test_alpha_lastName(self):
        self.__lastName = "PIY"
        lastNameObj = LastNameValidation(self.__lastName, 2, 20)
        self.assertEqual(True, lastNameObj.alpha_validation())

    def test_lefttrim_lastName(self):
        self.__lastName = "Imtiyaz"
        lastNameObj = LastNameValidation(self.__lastName, 2, 20)
        self.assertEqual(True, lastNameObj.left_trim_validation())

    def test_mobile(self):
        self.__mobile = "1221211234"
        mobileObj = MobileValidation(self.__mobile, 10, 20)
        self.assertEqual(True, mobileObj.validation())

    def test_min_mobile(self):
        self.__mobile = "1221211234"
        mobileObj = MobileValidation(self.__mobile, 8, 20)
        self.assertEqual(True, mobileObj.min_validation())

    def test_max_mobile(self):
        self.__mobile = "1221211234"
        mobileObj = MobileValidation(self.__mobile, 10, 20)
        self.assertEqual(True, mobileObj.max_validation())

    def test_req_mobile(self):
        self.__mobile = "1221211234"
        mobileObj = MobileValidation(self.__mobile, 10, 20)
        self.assertEqual(True, mobileObj.req_validation())

    def test_left_mobile(self):
        self.__mobile = "1221211234"
        mobileObj = MobileValidation(self.__mobile, 10, 20)
        self.assertEqual(True, mobileObj.left_trim_validation())

    def test_number(self):
        self.__number = "1221211234"
        numberObj = NumberValidation(self.__number)
        self.assertEqual(True, numberObj.validation())

    def test_password(self):
        self.__password = "@Imtiyaz1234"
        passwordObj = PasswordValidation(self.__password, 8, 12)
        self.assertEqual(True, passwordObj.validation())

    def test_max_password(self):
        self.__password = "@Imtiyaz1234"
        passwordObj = PasswordValidation(self.__password, 8, 19)
        self.assertEqual(True, passwordObj.max_validation())

    def test_min_password(self):
        self.__password = "@Imtiyaz1234"
        passwordObj = PasswordValidation(self.__password, 8, 12)
        self.assertEqual(True, passwordObj.min_validation())

    def test_req_password(self):
        self.__password = "Imtiyaz1234"
        passwordObj = PasswordValidation(self.__password, 8, 12)
        self.assertEqual(True, passwordObj.req_validation())

    def test_alphanumeric_password(self):
        self.__password = "Imtiyaz1234"
        passwordObj = PasswordValidation(self.__password, 8, 12)
        self.assertEqual(True, passwordObj.alpha_numeric())

    def test_left_trim_password(self):
        self.__password = "@Imtiyaz1234"
        passwordObj = PasswordValidation(self.__password, 8, 12)
        self.assertEqual(True, passwordObj.left_trim_validation())

    def test_employeecode(self):
        self.__password = "@Imtiyaz1234"
        passwordObj = PasswordValidation(self.__password, 8, 12)
        self.assertEqual(True, passwordObj.validation())

    def test_max_employeecode(self):
        self.__password = "@Imtiyaz1234"
        passwordObj = PasswordValidation(self.__password, 8, 19)
        self.assertEqual(True, passwordObj.max_validation())

    def test_min_employeecode(self):
        self.__password = "@Imtiyaz1234"
        passwordObj = PasswordValidation(self.__password, 8, 12)
        self.assertEqual(True, passwordObj.min_validation())

    def test_req_employeecode(self):
        self.__password = "Imtiyaz1234"
        passwordObj = PasswordValidation(self.__password, 8, 12)
        self.assertEqual(True, passwordObj.req_validation())

    def test_alphanumeric_employeecode(self):
        self.__password = "Imtiyaz1234"
        passwordObj = PasswordValidation(self.__password, 8, 12)
        self.assertEqual(True, passwordObj.alpha_numeric())

    def test_left_employeecode(self):
        self.__password = "@Imtiyaz1234"
        passwordObj = PasswordValidation(self.__password, 8, 12)
        self.assertEqual(True, passwordObj.left_trim_validation())


    def test_zipCode(self):
        self.__zipCode = '1234567'
        zipCodeObj = ZipCodeValidation(self.__zipCode)
        self.assertEqual(True, zipCodeObj.validation())

    def test_confirmpassword(self):
        self.__password = '12345678'
        self.__confirm_password = '12345678'
        passobj = ConfirmPasswordValidaton(self.__password, self.__confirm_password, 8, 16)
        self.assertEqual(True, passobj.validation())

    def test_max_confirmpassword(self):
        self.__password = '12345678'
        self.__confirm_password = '12345678'
        passobj = ConfirmPasswordValidaton(self.__password, self.__confirm_password, 8, 16)
        self.assertEqual(True, passobj.max_validation())

    def test_min_confirmpassword(self):
        self.__password = '12345678'
        self.__confirm_password = '12345678'
        passobj = ConfirmPasswordValidaton(self.__password, self.__confirm_password, 6, 16)
        self.assertEqual(True, passobj.min_validation())

    def test_req_confirmpassword(self):
        self.__password = '12345678'
        self.__confirm_password = '12345678'
        passobj = ConfirmPasswordValidaton(self.__password, self.__confirm_password, 8, 16)
        self.assertEqual(True, passobj.req_validation())

    def test_lefttrim_confirmpassword(self):
        self.__password = '12345678'
        self.__confirm_password = '12345678'
        passobj = ConfirmPasswordValidaton(self.__password, self.__confirm_password, 8, 16)
        self.assertEqual(True, passobj.validation())

    def test_alphanumeric_confirmpassword(self):
        self.__password = 'piyoosh12345678'
        self.__confirm_password = '12345678'
        passobj = ConfirmPasswordValidaton(self.__password, self.__confirm_password, 8, 16)
        self.assertEqual(True, passobj.alpha_numeric())

    def test_req_address(self):
        self.address = "dsfdsf12fdsfdjff,GHA"
        address = AddressValidation(self.address, 8, 12)
        self.assertEqual(True, address.req_validation())

    def test_notempty_address(self):
        self.address = "dsfdsf12fdsfdjff,GHA"
        address = AddressValidation(self.address, 8, 12)
        self.assertEqual(True, address.notempty_validation())


    def test_alphanumeric(self):
        self.__number = 'numbrer1'
        obj = AlphaNumericCheckValidation(self.__number)
        self.assertEqual(True, obj.validation())

    def test_alphacheck(self):
        self.__number = 'SSS'
        obj = AlphaCheckValidation(self.__number)
        self.assertEqual(True, obj.validation())

    def test_maxdate(self):
        self.__date1 = "01/01/2016"
        self.__date2 = "31/12/2015"
        obj = MaximumDateValdiation(self.__date1, self.__date2)
        self.assertEqual(True, obj.validation())

    def test_mindate(self):
        self.__date1 = "31/12/2015"
        self.__date2 = "01/01/2016"
        obj = MinimumDateValdiation(self.__date1, self.__date2)
        self.assertEqual(True, obj.validation())

# Create your tests here.

USERDATA_1 = {
    "email": "fd@gmail.com",
    "emp_code": "password"
}


class UserTest(APITestCase):
    """Test case are here """

    def setUp(self):
        self.client = APIClient()

        self.signup = AudioApp.models.MyUser.objects.create(email='fd@gmail.com')
        self.signup.set_password('password')
        self.signup.is_active = True
        self.signup.save()

        self.signup1 = AudioApp.models.MyUser.objects.create(email='piyoosh.kumar@mobiloitte.in')
        self.signup1.set_password('password')
        self.signup1.is_active = True
        self.signup1.save()

        self.company = AudioApp.models.Companies.objects.create(street='dsf', state='updd', country='India', zipcode=231213,
                                                                representative_email='Mobiloitte@gmail.com', password='Mobiloitte1')

        self.employee = AudioApp.models.Employess.objects.create(employee_email='fd@gmail.com', employee_code='password',
                                                                 employee_id=113,
                                                                 firstname='emp1', lastname='last', jobtitle='fdgdf',
                                                                 company=self.company, date_time=date.today())

        self.employee1 = AudioApp.models.Employess.objects.create(employee_email='piyoosh.kumar@mobiloitte.in',
                                                                  employee_code='password', employee_id=123,
                                                                  firstname='emp1', lastname='last', jobtitle='fdgdf',
                                                                  company=self.company, date_time=date.today())

        self.Lesson = AudioApp.models.Lessons.objects.create(lesson_name='lesson1', created_on='2018-01-09')

        self.chapter = AudioApp.models.Chapters.objects.create(lesson=self.Lesson, chapter_name='chapter1',
                                                               chapter='01_-_Aaj_Se_Teri_128_Kbps_-_DownloadMing.SE_ZL53Pbt.mp3')

        self.Companylesson = AudioApp.models.CompanyLesson.objects.create(lesson=self.Lesson, company=self.company, Employee_slot=10,
                                                                          expiry_date='2018-01-09')

        self.Employeelesson = AudioApp.models.EmployeeLesson.objects.create(lesson=self.Lesson, progress='complete',
                                                                            employee=self.employee)

        self.token = self.client.post('/audio/login', data={"email": "fd@gmail.com", "emp_code": "password"})

        self.token2 = self.client.post('/audio/login',
                                       data={"email": "piyoosh.kumar@mobiloitte.in", "emp_code": "password"})

    def test_login(self):
        response = self.client.post('/audio/login', data={"email": "fd@gmail.com", "emp_code": "password"})
        response2 = self.client.post('/audio/login',
                                     data={"email": "piyoosh.kumar@mobiloitte.in", "emp_code": "password"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

    def test_lessons(self):
        response = self.client.post('/audio/lessons', HTTP_AUTHORIZATION='JWT {}'.format(self.token.data.get('token')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Chapters(self):
        response = self.client.get('/audio/Chapters/{}'.format(self.Lesson.id),
                                   HTTP_AUTHORIZATION='JWT {}'.format(self.token.data.get('token')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_updatelesson(self):
        response = self.client.put('/audio/updatelesson/{}'.format(self.Employeelesson.id),
                                   data={"progress": "incomplete"},
                                   HTTP_AUTHORIZATION='JWT {}'.format(self.token.data.get('token')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


