from django import forms
from django.forms import ModelForm
# from registration.forms import RegistrationForm
from .models import Artist, Song, Album, Playlist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from django.contrib.auth.models import User  # , UserModel
# from django.contrib.auth.forms import UserCreationForm
# from registration.forms import RegistrationForm
# from django.users import UserModel  # , UserNameField


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


"""
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.password = forms.CharField(widget=forms.PasswordInput)
"""


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    topic = forms.CharField(max_length=500)


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        exclude = ()


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ()


class SongForm(ModelForm):
    class Meta:
        model = Song
        exclude = ()


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ()
