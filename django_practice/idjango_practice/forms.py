from django import forms
from django.forms import ModelForm
# from registration.forms import RegistrationForm
from .models import Artist, Song, Album, Playlist, OwnUser
from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.models import User  # , UserModel
# from django.contrib.auth.forms import UserCreationForm
# from registration.forms import RegistrationForm
# from django.users import UserModel  # , UserNameField


class RegisterForm(UserCreationForm):
    # __metaclass__ = classmaker()
    class Meta:
        
        email = forms.EmailField(required=True)
        first_name = forms.CharField(required=False)
        last_name = forms.CharField(required=False)

        model = OwnUser
        fields = ()
        exclude = ("id_user", "user_id")


class LoginForm(forms.Form):
    pass


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
