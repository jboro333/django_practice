from django.shortcuts import render
# from .forms import NormalUserForm
# from django.template import RequestContext
from .models import NormalUser  # ArtistUser
from django.views.generic import DetailView


# Create your views here.
class Home(DetailView):
    model = NormalUser
    # template =


def home(request):
    return render(request, "home.html", {})
