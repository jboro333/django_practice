from django import forms
from django.forms import ModelForm
from idjango_practice.models import NormalUser, ArtistUser


class RegisterForm(forms.Form):
    pass


class PlaylistForm(ModelForm):
    pass


class AlbumForm(ModelForm):
    pass


class SongForm(ModelForm):
    pass


class ArtistUserForm(ModelForm):
    model = ArtistUser


class NormalUserForm(ModelForm):
    model = NormalUser
