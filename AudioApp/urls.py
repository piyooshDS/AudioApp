""" file for urls"""
import django.conf.urls

from AudioApp.views import Login, EmployeeLessonAPI, ForgotCode, UpdateLesson, Chapterlist, IntroView, MyChapter

urlpatterns = [
    django.conf.urls.url(r'login', Login.as_view()),
    django.conf.urls.url(r'lessons', EmployeeLessonAPI.as_view()),
    django.conf.urls.url(r'forgotcode', ForgotCode.as_view()),
    django.conf.urls.url(r'updatelesson/(?P<pk>[0-9]+)$', UpdateLesson.as_view()),
    django.conf.urls.url(r'Chapters/(?P<pk>[0-9]+)$', Chapterlist.as_view()),
    django.conf.urls.url(r'get-chapter/(?P<pk>[0-9]+)$', MyChapter.as_view()),
    django.conf.urls.url(r'Intro', IntroView.as_view()),

]
