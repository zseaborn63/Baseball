from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from Django_Stats.models import Player


def index(request):
    return render_to_response('index.html')

class PlayerListView(ListView):
    model = Player
