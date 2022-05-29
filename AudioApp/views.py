""" file for views"""
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import loader
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from .models import Lessons, EmployeeLesson, Chapters, Employess, Intro,CompanyLesson,ChapterEmployee
from .serializers import MyUserserializer, EmployeeLessonSerializer, ChapterSerializer, ChapterStatusSerializer, \
    IntroSerializer
from datetime import datetime

# # Create your views here.
class Login(APIView):
    """
    API for Employee login
    """

    def post(self, request):
        """ post method """
        user = authenticate(email=request.data['email'], password=request.data['emp_code'])
        if user:
            serializer = MyUserserializer(user)
            return Response(
                {"message": "Logged In successfully!!", "token": user.create_jwt(), "data": serializer.data},
                status=HTTP_200_OK)
        return Response({"message": "Please provide the correct credentials!!"}, status=HTTP_400_BAD_REQUEST)


class EmployeeLessonAPI(APIView):
    """
    API for Retreiving lessons assigned to employee
    """

    # permission_classes=(IsAuthenticated, )
    def post(self, request):
        """ post method """
        user = request.user
        lessons = list(EmployeeLesson.objects.filter(employee__employee_email=user, is_access=True).values_list('lesson', flat=True))
        if not len(lessons):
            return Response({"message": "You do not have any Lessons available. Please contact your administrator."}, status=HTTP_200_OK)
        les=list(CompanyLesson.objects.filter(company=user.company,lesson__id__in=lessons, expiry_date__gte=datetime.now()).values_list('lesson', flat=True))
        emp_data=EmployeeLesson.objects.filter(lesson__id__in=les,employee__employee_email=user).distinct()
        if not len(emp_data):
            return Response({"message": "The lessons have expired. Please contact your administrator."}, status=HTTP_200_OK)
        serializer = EmployeeLessonSerializer(emp_data, many=True)
        return Response({"message": "Lessons Retrieved Successfully!!", "data": serializer.data}, status=HTTP_200_OK)


class UpdateLesson(RetrieveUpdateAPIView):
    """ update Lesson progress """
    queryset = EmployeeLesson.objects.all()
    serializer_class = EmployeeLessonSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        """ post method """
        try:
            instance = EmployeeLesson.objects.get(lesson_id=kwargs['pk'])
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Lesson updated Successfully."}, status=HTTP_200_OK)
        except:
            return Response(status=HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        """ post method """
        try:
            instance = EmployeeLesson.objects.get(lesson_id=kwargs['pk'])
            serializer = self.get_serializer(instance)
            return Response({"message": "Lesson details.", "data": serializer.data}, status=HTTP_200_OK)
        except:
            return Response(status=HTTP_404_NOT_FOUND)


class Chapterlist(RetrieveUpdateAPIView):
    """ Chapterlist class """
    permission_classes = (IsAuthenticated,)
    queryset = Lessons.objects.all()
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        """ post method """
        params=request.data
        instance = Chapters.objects.get(pk=kwargs['pk'])
        serializer = ChapterStatusSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        employee=Employess.objects.get(employee_email=request.user)
        print(employee.pk)
        chapteremp=ChapterEmployee.objects.update_or_create(lesson_id=params['lesson_id'],chapter=instance,employee_id=employee.pk)
        return Response({"message": "Chapter  updated Successfully.", "data": serializer.data}, status=HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """ post method """
        instance = self.get_object()
        token = request.META.get('HTTP_AUTHORIZATION')
        self.queryset = Chapters.objects.filter(lesson=instance).order_by('created_at')
        unlock = Chapters.objects.get(chapter_name=self.queryset[0], lesson=self.queryset[0].lesson)
        unlock.status = "Unlocked"
        unlock.save()
        self.queryset = Chapters.objects.filter(lesson=instance).order_by('created_at')
        serializer = ChapterSerializer(self.queryset, many=True, context={"token": token, "request": request})
        return Response({"message": "Chapters Retrieved Successfully!!", "data": serializer.data}, status=HTTP_200_OK)


class MyChapter(RetrieveUpdateAPIView):
    """ Chapterlist class """
    permission_classes = (IsAuthenticated,)
    queryset = Chapters.objects.all()
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        """ post method """
        "fdgfdgfdgfdg"
        instance = self.get_object()
        token = request.META.get('HTTP_AUTHORIZATION')
        serializer = ChapterSerializer(instance, context={"token": token, "request": request})
        return Response({"message": "Chapter details.", "data": serializer.data}, status=HTTP_200_OK)


class ForgotCode(APIView):
    """
    API to request employee code
    """

    def post(self, request):
        """ post method """
        try:
            email = request.data['email']

            employee = Employess.objects.get(employee_email=email)
            context = {'user': employee, 'passcode': employee.employee_code}
            message = loader.get_template('Forgot_code.html').render(context)
            msg = EmailMessage("iAudio passcode", message, 'iAudio_App<a@a.com>', to=[employee.employee_email])
            msg.content_subtype = "html"
            msg.send()
            return Response({"message": "Mail sent successfully."}, status=HTTP_200_OK)
        except:
            return Response({"message": "User does not exist"}, status=HTTP_400_BAD_REQUEST)


class IntroView(APIView):
    """docstring for IntoView Class """

    def get(self, request):
        terms = Intro.objects.filter(id=1)
        token = "12345678910111213141516"
        serializer = IntroSerializer(terms, many=True, context={"token": token, "request": request})
        return Response({"data": serializer.data}, status=HTTP_200_OK)


def Access(request, lesson, pk):
    """
       API to request employee code
    """
    emplesson = EmployeeLesson.objects.get(pk=pk)
    if emplesson.is_access:
        emplesson.is_access = False
    else:
        emplesson.is_access = True
    emplesson.save()
    return redirect("/admin/AudioApp/lessons/{}/change/".format(lesson))
