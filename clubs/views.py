from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Club

# Create your views here.


class ClubListView(ListView):
    def get_queryset(self):
        return Club.objects.all()


class ClubDetailsView(DetailView):

    model = Club

    def get_context_data(self, **kwargs):
        context = super(ClubDetailsView, self).get_context_data(**kwargs)
        return context