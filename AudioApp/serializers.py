""" your serializers here """
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from rest_framework.fields import CurrentUserDefault

from .encryption import encrypt_file
from .models import MyUser, Lessons, EmployeeLesson, Chapters, Intro,ChapterEmployee


class MyUserserializer(serializers.ModelSerializer):
    """ model for User  Serializer"""

    class Meta:
        """ docstring for meta"""
        model = MyUser
        fields = ["id", "email"]


class LessonsSerializer(serializers.ModelSerializer):

    logo = SerializerMethodField()
    percentage_status = SerializerMethodField()

    def get_logo(self, obj):
        """ method for get logo """
        if obj.logo:
            return obj.logo.build_url()
        return None

    def get_percentage_status(self, obj):
        if obj:
            total = Chapters.objects.filter(lesson=obj).count()
            print(total)
            # completed = Chapters.objects.filter(lesson=obj, is_complete=True).count()
            completed=ChapterEmployee.objects.filter(employee_id=self.context.get('emp'),is_complete=True,lesson_id=obj.id).count()
            print(completed)
            try:
                percentage = (completed / total) * 100
                percentage=round(percentage,2)
            except Exception as e:
                print(e)
                percentage=total
            print(percentage)
            return str(percentage)

        return ""

    class Meta:
        """ docstring for meta"""
        model = Lessons
        fields = "__all__"


class EmployeeLessonSerializer(serializers.ModelSerializer):

    lesson1 =SerializerMethodField()

    def get_lesson1(self,obj):
        return LessonsSerializer(obj.lesson,context={"emp":obj.employee.id}).data


    class Meta:
        """ docstring for meta"""
        model = EmployeeLesson
        fields = "__all__"


class ChapterSerializer(serializers.ModelSerializer):
    """ model for Chapter Lesson Serializer"""

    chapter = SerializerMethodField()
    lesson = SerializerMethodField()
    lesson_id=SerializerMethodField()

    def get_lesson_id(self, obj):
        if obj:
            return obj.lesson.id
        return ""

    def get_lesson(self, obj):
        if obj:
            return obj.lesson.lesson_name
        return ""

    def get_chapter(self, obj):
        """ method for get chapter"""
        return encrypt_file(self.context.get("token"), obj.chapter, self.context.get("request"))

    class Meta:
        """ docstring for meta"""
        model = Chapters
        fields = "__all__"


class ChapterStatusSerializer(serializers.ModelSerializer):
    """ model for Chapter Lesson Serializer"""
    lesson = SerializerMethodField()
    lesson_id=SerializerMethodField()


    def get_lesson(self, obj):
        if obj:
            return obj.lesson.lesson_name
        return ""

    def get_lesson_id(self, obj):
        if obj:
            return obj.lesson.id
        return ""


    class Meta:
        """ docstring for meta"""
        model = Chapters
        fields = ('id', 'lesson', 'lesson_id','chapter_name', 'status', 'is_complete')


class IntroSerializer(serializers.ModelSerializer):
    """ docstring for Intro Class"""
    chapter = SerializerMethodField()

    def get_chapter(self, obj):
        return obj.chapter.build_url()

    class Meta:
        """ docstring for meta class"""
        model = Intro
        exclude = ('id',)
