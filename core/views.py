from django.shortcuts import render
from django.views.generic import ListView

from .models import Picture

class PictureListView(ListView):
    template_name = "core/list.html"
    model = Picture
