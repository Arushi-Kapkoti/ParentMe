from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout as logouts
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form 
from django import forms  
from django.contrib.auth.models import User 

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

class RegisterPage(FormView):
    template_name = 'main/registerOrphanage.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('OrphanList')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
# class CustomUserCreationForm(UserCreationForm):  
#     username = forms.CharField(label='username', min_length=5, max_length=150)  
#     email = forms.EmailField(label='email')  
#     password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
  
#     def username_clean(self):  
#         username = self.cleaned_data['username'].lower()  
#         new = User.objects.filter(username = username)  
#         if new.count():  
#             raise ValidationError("User Already Exist")  
#         return username  
  
#     def email_clean(self):  
#         email = self.cleaned_data['email'].lower()  
#         new = User.objects.filter(email=email)  
#         if new.count():  
#             raise ValidationError(" Email Already Exist")  
#         return email  
  
#     def clean_password2(self):  
#         password1 = self.cleaned_data['password1']  
#         password2 = self.cleaned_data['password2']  
  
#         if password1 and password2 and password1 != password2:  
#             raise ValidationError("Password don't match")  
#         return password2  
  
#     def save(self, commit = True):  
#         user = User.objects.create_user(  
#             self.cleaned_data['username'],  
#             self.cleaned_data['email'],  
#             self.cleaned_data['password1']  
#         )  
#         return user  

# def RegisterAddress(request):  
#     if request.POST == 'POST':  
#         form = CustomUserCreationForm()  
#         if form.is_valid():  
#             form.save()  
#     else:  
#         form = CustomUserCreationForm()  
#     context = {  
#         'form':form  
#     }  
#     return render(request, 'main/registerOrphanage.html', context)  

class OrphanList(LoginRequiredMixin, ListView):
    model = Orphan
    context_object_name = 'Orphans'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Orphans'] = context['Orphans'].filter(orphanage=self.request.user)
        return context

class OrphanDetails(LoginRequiredMixin, DetailView):
    model = Orphan
    context_object_name = 'orphan'

class AddOrphan(LoginRequiredMixin, CreateView):
    model = Orphan
    fields = ['name','child_image','description','age']
    template_name = 'main/AddOrphan.html'
    success_url = reverse_lazy('OrphanList')
    def form_valid(self, form):
        form.instance.orphanage = self.request.user
        return super(AddOrphan, self).form_valid(form)

class UpdateOrphanDetails(LoginRequiredMixin, UpdateView):
    model = Orphan
    fields = '__all__'
    template_name = 'main/AddOrphan.html'
    success_url = reverse_lazy('OrphanList')

class RemoveOrphan(LoginRequiredMixin, DeleteView):
    model = Orphan
    context_object_name = 'orphan'
    template_name = 'main/RemoveOrphan.html'
    success_url = reverse_lazy('OrphanList')

class AdoptMe(ListView):
    model = Orphan
    template_name = 'main/AdoptMe.html'
    context_object_name = 'Orphans'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['Orphans'] = context['Orphans'].filter(age__icontains=search_input)
        context['search_input']=search_input
        return context