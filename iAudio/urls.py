""" your urls here """
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from iAudio import settings
from AudioApp.views import *

admin.site.site_url = None

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', admin.site.urls),
    url(r'^djrichtextfield/', include('djrichtextfield.urls')),
    url(r'^audio', include('AudioApp.urls', namespace="AudioApp")),
    url(r'^static-files', include('Static_Management.urls', namespace="Static_Management")),
    url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', auth_views.password_reset_done,
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'admin/AudioApp/lessons/(?P<lesson>[0-9]+)/change/active/(?P<pk>[0-9]+)$', Access)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
