from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout as logouts
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import Orphan
# Create your views here.
def landingPage(request):
    return render(request,'main/landingPage.html')

class CustomLoginView(LoginView):
    template_name = 'main/loginOrphanage.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('OrphanList')

def logoutOrphanage(request):
    if request.method=='GET':
        logouts(request)
        return redirect('login-orphanage')

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

class UpdateOrphanDetails(UpdateView):
    model = Orphan
    fields = '__all__'
    template_name = 'main/AddOrphan.html'
    success_url = reverse_lazy('OrphanList')

class RemoveOrphan(DeleteView):
    model = Orphan
    context_object_name = 'orphan'
    template_name = 'main/RemoveOrphan.html'
    success_url = reverse_lazy('OrphanList')