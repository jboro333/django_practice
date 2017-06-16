"""django_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib.auth import login_required

# from rest_framework.urlpatterns import format_suffix_patters
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
# from model import Playlist, Song, Album, Artist, Review
# from accounts.views import (login_view, register_view, logout_view)

from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from idjango_practice import views
from django.views.generic import ListView  # DetailView, UpdateView
from rest_framework.urlpatterns import format_suffix_patterns
from idjango_practice.forms import *
from idjango_practice.models import Playlist, Artist, Song, Album
from idjango_practice.serializers import *
from idjango_practice.views import review

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^home', views.home, name="home"),
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^contact', views.contact, name="contact"),
    url(r'^musica/', include('idjango_practice.urls', namespace='idjango_practice')),
    url(r'^admin/', admin.site.urls)
]

"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
