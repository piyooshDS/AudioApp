""" docstring """
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView

from AudioApp.models import *
from .serializers import *


# Create your views here.
# @csrf_exempt
class AboutUsAPI(APIView):
    """
    API for Retreiving AboutUs of company
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """ docstring """
        user = request.user.email
        try:
            employee = Employess.objects.get(employee_email=user)
            about_us = AboutUs.objects.get(company=employee.company)
            serializer = AboutUsSerializer(about_us)
            return Response({"message": "AboutUs Retrieved Successfully!!", "data": serializer.data},
                            status=HTTP_200_OK)
        except:
            return Response({"message": "AboutUs Not Found!!"}, status=HTTP_404_NOT_FOUND)


class TermsServicesAPI(APIView):
    """
    API for Retreiving TermsServices of company
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """ docstring """
        user = request.user.email
        try:
            employee = Employess.objects.get(employee_email=user)
            term_services = TermServices.objects.get(company=employee.company)
            serializer = TermServicesSerializer(term_services)
            return Response({"message": "Terms and Services Retrieved Successfully!!", "data": serializer.data},
                            status=HTTP_200_OK)
        except:
            return Response({"message": "Terms and Services Not Found!!"}, status=HTTP_404_NOT_FOUND)


class PrivacyPolicyAPI(APIView):
    """
    API for Retreiving PrivacyPolicy of company
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """ docstring """
        user = request.user.email
        try:
            employee = Employess.objects.get(employee_email=user)
            privacy_policy = PrivacyPolicy.objects.get(company=employee.company)
            serializer = PrivacyPolicySerializer(privacy_policy)
            return Response({"message": "Privacy Policy Retrieved Successfully!!", "data": serializer.data},
                            status=HTTP_200_OK)
        except:
            return Response({"message": "Privacy Policy not Found!!"}, status=HTTP_404_NOT_FOUND)
