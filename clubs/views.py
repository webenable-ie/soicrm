from django.shortcuts import render
from django.views.generic import ListView

from .models import Club

# Create your views here.


class ClubList(ListView):
    def get_queryset(self):
        return Club.objects.all()
