from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.
class PollList(ListView):
    model=Poll
    template_name ='default/poll_list.html'