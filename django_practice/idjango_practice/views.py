# from django.template.context import RequestContext
from models import Song, Playlist, Artist, Album
# from forms import AlbumForm, SongForm, PlaylistForm, Artistform
from django_practice import settings
from .forms import ContactForm, UserForm, UserLoginForm
from forms import SongForm, AlbumForm, PlaylistForm, ArtistForm
from serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from serializers import PlaylistSerializer
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, DetailView, FormView
from django.views.generic import View
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, render_to_response, get_object_or_404
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
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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
    return HttpResponseRedirect(settings.LOGIN_URL)
    # SI VOLEM QUE TORNI A HOME AL FER LOGOUT:
    # return redirect('../home')


def home(request):
    return render(request, "home.html", {})


"""
def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned.data.get("username")
        password = form.cleaned.data.get('password')

    return render(request, "form.html", {"form": form, "title": title})


def register_view(request):
    return render(request, "form.html", {})


def logout_view(request):
    return render(request, "form.html", {})
"""

"""
class UserFormView(object):
    form_class = UserForm
    template_name = 'idjango_practice/register.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process
    def post(self, request):
        form = self.form_class(request.POST)
        # quan cliquin a submit, aqui es guardara

        if form.is_Valid():

            user = form.save(commit=False)  # x no guardarho encara

            # parsejar xk ho agafi be
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)  # cambiar la pw del usuari
            user.save()

            # si les credencials OK , retorna user
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('views.home')
        return render(request, self.template_name, {'form': form})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'idjango_practice/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'idjango_practice/home.html', {'albums': albums})
            else:
                return render(request, 'idjango_practice/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'idjango_practice/login.html', {'error_message': 'Invalid login'})
    return render(request, 'idjango_practice/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'home.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)



"""


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
    return render(request, "register.html", context


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
"""


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


=======
>>>>>>> 0a64de0cf32077da44d03943373f82ce68bb5098
def contact(request):
    form = ContactForm
    context = {
        "contact_form": form
    }
    return render(request, "contact.html", context)


"""
def register(request):
    form = RegisterForm
    context = {
        "register_form": form
    }
    return render(request, "register.html", context)
"""


class PlaylistDetail(DetailView):
    model = Playlist
    template_name = 'youridjango_practice/playlist_detail.html'

    def get_context(self, **kwargs):
        context = super(PlaylistDetail, self).get_context_data(**kwargs)
        return context


class PlaylistCreate(CreateView):
    model = Playlist
<<<<<<< HEAD
    template_name = 'youridjango_practice/playlist_create.html'
=======
    template_name = 'playlist.html'
>>>>>>> 0a64de0cf32077da44d03943373f82ce68bb5098
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
        """
    def song_review(request, pk):
<<<<<<< HEAD
        artist = get_object
        """
=======
        # artist = get_object
        pass
>>>>>>> 0a64de0cf32077da44d03943373f82ce68bb5098


# clase vista
class SongCreate(CreateView):
    model = Song
<<<<<<< HEAD
    template_name = 'idjango_practice/playlist_create.html'
=======
    template_name = 'song.html'
>>>>>>> 0a64de0cf32077da44d03943373f82ce68bb5098
    form_class = SongForm
    success_url = '/song_created'

    # funcion vista
    def form_valid(self, form):
        # self.object = form.save()
        return super(SongCreate, self).form_valid(form)


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'idjango_practice/artist_detail.html'

    def get_context(self, **kwargs):
        context = super(ArtistDetail, self).get_context_data(**kwargs)
        return context


class ArtistCreate(CreateView):
    model = Artist
<<<<<<< HEAD
    template_name = 'idjango_practice/artist_create.html'
=======
    template_name = 'artist.html'
>>>>>>> 0a64de0cf32077da44d03943373f82ce68bb5098
    form_class = ArtistForm
    success_url = '/artist_created'

    def form_valid(self, form):
        # return super(ArtistCreate, self).form_valid(form)
        result = super(ArtistCreate, self).form_valid(form)
        return result


class AlbumDetail(DetailView):
    model = Album
<<<<<<< HEAD
    template_name = 'idjango_practice/album_detail.html'
=======
    template_name = 'yourmusic/album.html'
>>>>>>> 0a64de0cf32077da44d03943373f82ce68bb5098

    def get_context(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        return context


class AlbumCreate(CreateView):
    model = Album
<<<<<<< HEAD
    template_name = 'idjango_practice/album_create.html'
=======
    template_name = 'album.html'
>>>>>>> 0a64de0cf32077da44d03943373f82ce68bb5098
    form_class = AlbumForm
    success_url = '/album_created'

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super(AlbumCreate, self).form_valid(form)


"""
def artistCreate(request):
    form = ArtistForm(request.POST)
    form_data = form.cleaned_data()  # obtenemos la info del formulario
    obj = Artist()
    obj.name_artist = form_data.get("name_artist")
    # obj.sport_type = form_data.get("sport_type")
    obj.date = date.today()
    # obj.user = request.user.id
    obj.save()
    context = {
        'form': form
    }
    return render(request, 'artist.html', context)
"""
# API views


class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class APIArtistList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_context(self, **kwargs):
        context = super(ArtistDetail, self).get_context_data(**kwargs)
        return context


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
