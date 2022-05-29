""" docstring """
from datetime import date

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from AudioApp.models import *
from .models import *

# Create your tests here.

USERDATA_1 = {
    "email": "fd@gmail.com",
    "emp_code": "password"
}


class StaticTest(APITestCase):
    """Test case are here """

    def setUp(self):
        """ docstring """
        self.client = APIClient()
        self.signup = MyUser.objects.create(email='fd@gmail.com')
        self.signup.set_password('password')
        self.signup.is_active = True
        self.signup.save()
        self.company = Companies.objects.create(street='dsf', state='updd', country='India', zipcode=231213,
                                                representative_email='Mobiloitte@gmail.com', password='Mobiloitte1')

        self.employee = Employess.objects.create(employee_email='fd@gmail.com', employee_code='password',
                                                 employee_id=113,
                                                 firstname='emp1', lastname='last', jobtitle='fdgdf',
                                                 company=self.company, date_time=date.today())

        self.about = AboutUs.objects.create(company=self.company, heading='AboutUs', content='Lorem Ipsum About us')
        self.term = TermServices.objects.create(company=self.company, heading='TermServices',
                                                content='Lorem Ipsum Terms and Services')
        self.privacy = PrivacyPolicy.objects.create(company=self.company, heading='PrivacyPolicy',
                                                    content='Lorem Ipsum PrivacyPolicy')

        self.token = self.client.post('/audio/login', data={"email": "fd@gmail.com", "emp_code": "password"})

    def test_login(self):
        """ docstring """
        response = self.client.post('/audio/login', data={"email": "fd@gmail.com", "emp_code": "password"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_aboutUs(self):
        response = self.client.post('/static-files/aboutus',
                                    HTTP_AUTHORIZATION='JWT {}'.format(self.token.data.get('token')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_privacypolicy(self):
        response = self.client.post('/static-files/privacypolicy',
                                    HTTP_AUTHORIZATION='JWT {}'.format(self.token.data.get('token')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Termsservices(self):
        response = self.client.post('/static-files/termsservices',
                                    HTTP_AUTHORIZATION='JWT {}'.format(self.token.data.get('token')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
