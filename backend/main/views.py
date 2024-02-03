from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

from .models import Orphan
# Create your views here.
def landingPage(request):
    return render(request,'main/landingPage.html')

# def mainPage(request):
#     return render(request,'main/landingPage.html')

class OrphanList(ListView):
    model = Orphan
    context_object_name = 'Orphans'

class OrphanDetails(DetailView):
    model = Orphan
    context_object_name = 'orphan'

class AddOrphan(CreateView):
    model = Orphan
    fields = '__all__'
    template_name = 'main/AddOrphan.html'
    success_url = reverse_lazy('OrphanList')