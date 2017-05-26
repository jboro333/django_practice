from django import forms
from django.forms import ModelForm
# from registration.forms import RegistrationForm
from .models import Artist, Song, Album, Playlist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    topic = forms.CharField(max_length=500)


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ['name_playlist', 'user', 'songs']


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['name_album', 'artist']


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['name_song', 'artist', 'album']


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name_artist']
