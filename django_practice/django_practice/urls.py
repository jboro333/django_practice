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
from django.contrib import admin
# from django.contrib.auth.views import login, logout
from idjango_practice import views
# from idjango_practice.views import Register

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^login', views.login, name="login"),
    url(r'^register', views.register, name="register"),
    # url(r'^register', Register.as_view(), name='register'),
    url(r'^contact', views.contact, name="contact"),
    # url(r'^artist', ArtistDetail, name="artist"),
    # url(r'^song', views.song, name="song"),
    # url(r'^album', views.album, name="album"),
    # url(r'^playlist', views.playlist, name="playlist"),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    # url(r'^login', views.login, name="login")
]
