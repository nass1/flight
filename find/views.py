from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"
