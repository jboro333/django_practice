from django import forms
from django.forms import ModelForm
from .models import Artist
from django.contrib.auth.models import User  # , UserModel
from django.contrib.auth.forms import UserCreationForm
# from django.users import UserModel  # , UserNameField


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        exclude = ("last_login", "date_joined", "is_active", "is_staff", "la\
        st_name", "first_name", "is_superuser", "id")


class LoginForm(forms.Form):
    class Meta:
        form = 


class ContactForm(forms.Form):
    pass


class PlaylistForm(ModelForm):
    pass


class AlbumForm(ModelForm):
    pass


class SongForm(ModelForm):
    pass


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ()
