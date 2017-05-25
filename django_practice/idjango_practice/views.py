# from django.template.context import RequestContext
from models import Song, Playlist, Artist, Album
# from forms import AlbumForm, SongForm, PlaylistForm, Artistform
from forms import LoginForm, ContactForm, RegisterForm
from forms import SongForm, AlbumForm, PlaylistForm, ArtistForm
from serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from serializers import PlaylistSerializer
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic import CreateView, ListView, DetailView, FormView
from django.core.exceptions import PermissionDenied, permissions
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from rest_framework import permissions, generics
# from django.contrib.auth import login

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# from django.template import RequestContext
# from django.views.generic import DetailView
# from django.core import views as core_views


# Create your views here.
def home(request):
    return render(request, "home.html", {})


"""
class Register(CreateView):
    model = User
    templae_name = 'templates/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('')


def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        obj = User()
        obj.email = form_data.get("email")
        obj.password = form_data.get("password")
        obj.save()
    context = {
        "register_form": form
    }
    return render(request, "register.html", context)
"""


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data  # obtenemos la info del formulario
            obj = User()
            obj.name = form_data.get("name")
            obj.sport_type = form_data.get("sport_type")
            # obj.date = date.today()
            # si el usuario esta registrado:
            # else:
            obj.user = request.user.id
            obj.save()
    else:
        form = LoginForm()
    context = {
        "sport_session_form": form,
    }
    return render(request, "login.html", context)


def login2(request):
    form = LoginForm
    context = {
        "login_form": form
    }
    return render(request, "login.html", context)


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


def contact(request):
    form = ContactForm
    context = {
        "contact_form": form
    }
    return render(request, "contact.html", context)


class PlaylistDetail(DetailView):
    model = Playlist
    template_name = 'yourmusic/playlist_detail.html'

    def get_context(self, **kwargs):
        context = super(PlaylistDetail, self).get_context_data(**kwargs)
        return context


class PlaylistCreate(CreateView):
    model = Playlist
    template_name = 'yourmusic/playlist_create.html'
    form_class = PlaylistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlaylistCreate, self).form_valid(form)


class SongDetail(DetailView):
    model = Song
    template_name = 'yourmusic/song_detail.html'

    def get_context(self, **kwargs):
        context = super(SongDetail, self).get_context_data(**kwargs)
        return context

    def song_review(request, pk):
        artist = get_object


class SongCreate(CreateView):
    model = Song
    template_name = 'yourmusic/playlist_create.html'
    form_class = SongForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SongCreate, self).form_valid(form)


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'yourmusic/artist_detail.html'

    def get_context(self, **kwargs):
        context = super(ArtistDetail, self).get_context_data(**kwargs)
        return context


class ArtistCreate(CreateView):
    model = Artist
    template_name = 'yourmusic/artist_create.html'
    form_class = ArtistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ArtistCreate, self).form_valid(form)


class AlbumDetail(DetailView):
    model = Album
    template_name = 'yourmusic/album_detail.html'

    def get_context(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        return context


class AlbumCreate(CreateView):
    model = Album
    template_name = 'yourmusic/album_create.html'
    form_class = AlbumForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumCreate, self).form_valid(form)

# API views


class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class APIArtistList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class APIArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class APISongList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Song
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class APISongDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Song
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class APIPlaylistList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Playlist
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class APIPlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Playlist
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class APIAlbumList(generics.ListCreateAPIView):
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        model = Album
        queryset = Album.objects.all()
        serializer_class = AlbumSerializer


class APIAlbumDetail(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = (IsOwnerOrReadOnly,)
        model = Album
        queryset = Album.objects.all()
        serializer_class = AlbumSerializer
