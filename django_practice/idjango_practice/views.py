from django.shortcuts import render
from .forms import RegisterForm, LoginForm, ContactForm, ArtistForm, AlbumForm, SongForm, PlaylistForm
# from django.template import RequestContext
# from django.views.generic import DetailView


# Create your views here.
def home(request):
    return render(request, "home.html", {})


def register(request):
    form = RegisterForm()
    context = {
        "register_form": form
    }
    return render(request, "register.html", context)


def login(request):
    form = LoginForm
    context = {
        "login_form": form
    }
    return render(request, "login.html", context)


def contact(request):
    return render(request, "contact.hmtl", {})


def playlist(request):
    return render(request, "playlist.html", {})


def song(request):
    return render(request, "song.html", {})


def artist(request):
    return render(request, "artist.html", {})


def album(request):
    return render(request, "album.html", {})
