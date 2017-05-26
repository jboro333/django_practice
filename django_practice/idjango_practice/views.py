# from django.template.context import RequestContext
from models import Song, Playlist, Artist, Album
# from forms import AlbumForm, SongForm, PlaylistForm, Artistform
from django_practice import settings
from .forms import ContactForm, UserForm
from forms import SongForm, AlbumForm, PlaylistForm, ArtistForm

from serializers import ArtistSerializer, SongSerializer, PlaylistSerializer
from serializers import AlbumSerializer

from serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from serializers import PlaylistSerializer
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, DetailView, FormView
from django.views.generic import View
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, render_to_response, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
# from django.contrib.auth import login

from datetime import date
from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
#from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django import forms
# from django.template import RequestContext
# from django.views.generic import DetailView
# from django.core import views as core_views


# Create your views here.
def Login(request):
    # next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('../home')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "login.html", {'redirect_to': "home.html"})


def Logout(request):
    logout(request)
    # SI VOLEM QUE TORNI A LA PAGINA DE LOGIN ALM FER LOGOUT:
    # return HttpResponseRedirect(settings.LOGIN_URL)
    # SI VOLEM QUE TORNI A HOME AL FER LOGOUT:
    return redirect('../home')


def home(request):
    return render(request, "home.html", {})


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


def contact(request):
    form = ContactForm
    context = {
        "contact_form": form
    }
    return render(request, "contact.html", context)


class PlaylistDetail(DetailView):
    model = Playlist
    template_name = 'youridjango_practice/playlist_detail.html'

    def get_context(self, **kwargs):
        context = super(PlaylistDetail, self).get_context_data(**kwargs)
        return context


class PlaylistCreate(LoginRequiredMixin, CreateView):
    model = Playlist
    template_name = 'playlist.html'
    form_class = PlaylistForm
    success_url = '/playlist_created'

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super(PlaylistCreate, self).form_valid(form)


class SongDetail(DetailView):
    model = Song
    template_name = 'idjango_practice/song_detail.html'

    def get_context(self, **kwargs):
        context = super(SongDetail, self).get_context_data(**kwargs)
        return context


class SongCreate(LoginRequiredMixin, CreateView):
    model = Song
    template_name = 'song.html'
    form_class = SongForm

    def form_valid(self, form):
        # return super(ArtistCreate, self).form_valid(form)
        form.instance.user = self.request.user
        return super(SongCreate, self).form_valid(form)


"""
# clase vista
class SongCreate(LoginRequiredMixin, CreateView):
    form = SongForm
    # model = Song
    # template_name = 'post_form.html'
    # success_url = '../home'

    def form_valid(form):
        instance = form.save(commit=False)
        # print form.cleaned_data.get("title")
        instance.save()

        context = {
            "form": form,
        }
        return redirect(CreateView, "song.html", context)


    # funcion vista
    def form_valid(self, form):
        # self.object = form.save()
        form.instance.user = self.request.user
        super(SongCreate, self).form_valid(form)
        return redirect('../home')
"""


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'idjango_practice/artist_detail.html'

    def get_context(self, **kwargs):
        context = super(ArtistDetail, self).get_context_data(**kwargs)
        return context


class ArtistCreate(LoginRequiredMixin, CreateView):
    model = Artist
    template_name = 'artist.html'
    form_class = ArtistForm

    def form_valid(self, form):
        # return super(ArtistCreate, self).form_valid(form)
        form.instance.user = self.request.user
        return super(ArtistCreate, self).form_valid(form)


class AlbumDetail(DetailView):
    model = Album
    template_name = 'yourmusic/album.html'

    def get_context(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        return context


class AlbumCreate(LoginRequiredMixin, CreateView):
    model = Album
    template_name = 'album.html'
    form_class = AlbumForm
    success_url = '/album_created'

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super(AlbumCreate, self).form_valid(form)


# API views
class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class APIArtistList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    #def get_context(self, **kwargs):
    #    context = super(ArtistDetail, self).get_context_data(**kwargs)
    #    return context


class APIArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class APISongList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    model = Song
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class APISongDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly)
    model = Song
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class APIPlaylistList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    model = Playlist
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class APIPlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly)
    model = Playlist
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class APIAlbumList(generics.ListCreateAPIView):
        permission_classes = (permissions.IsAuthenticatedOrReadOnly)
        model = Album
        queryset = Album.objects.all()
        serializer_class = AlbumSerializer


class APIAlbumDetail(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = (IsOwnerOrReadOnly)
        model = Album
        queryset = Album.objects.all()
        serializer_class = AlbumSerializer
