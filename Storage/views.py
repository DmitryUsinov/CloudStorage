from typing import Any, Dict
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import FileForm, DisciplineForm, RegisterUserForm, LoginUserForm
from .models import Discipline, File
from .utils import *

def about(request):
    if request.user.is_authenticated:
        if not request.user.groups.all()[0].name == 'Преподаватель':
            menud = [{'title': "Главная", 'url_name': 'about'},
                {'title': "Дисциплины", 'url_name': 'discipline'}
                ]
        else:
            menud = [{'title': "Главная", 'url_name': 'about'},
        {'title': "Дисциплины", 'url_name': 'discipline'},
        ]
    else:
        menud = [{'title': "Главная", 'url_name': 'about'}]

    context = {'menu': menud }
    return render(request, 'Storage/about.html', context=context)

def disc_detail(request, id):
    posts = Discipline.objects.get(id=id)
    files = File.objects.filter(discipline_id=id)
    if not request.user.groups.all()[0].name == 'Преподаватель':
        menuf = [{'title': "Главная", 'url_name': 'about'},
         {'title': "Дисциплины", 'url_name': 'discipline'},
        ]
    else:      
        menuf = [{'title': "Главная", 'url_name': 'about'},
         {'title': "Дисциплины", 'url_name': 'discipline'},
        {'title': "Добавить файл", 'url_name': 'upload_file'},
        ]

    context = {
        'post': posts,
        'menu': menuf,
        'files': files
    }

    return render(request, 'Storage/disc_detail.html', context=context)

def logout_user(request):
    logout(request)
    return redirect('about')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'Storage/login.html'
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('discipline')
    

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'Storage/register.html'
    success_url = reverse_lazy('about')
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    

class DisciplineHome(DataMixin, ListView):
    model = Discipline
    template_name = 'Storage/home.html'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        
        return dict(list(context.items()) + list(c_def.items()))
    
    def deleteDiscipline(request, id):
    
        file = Discipline.objects.get(id=id)
        file.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class AddDiscipline(LoginRequiredMixin, DataMixin, CreateView):
    form_class = DisciplineForm
    template_name = 'Storage/add_discipline.html'
    success_url = reverse_lazy('discipline')
    login_url = reverse_lazy('discipline')

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        
        return dict(list(context.items()) + list(c_def.items()))

@login_required()
def model_form_upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['upload']
        form = FileForm(request.POST, request.FILES, uploaded_file)
        
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/discipline/')
    else:
        form = FileForm()
    return render(request, 'Storage/upload_file.html', {
        'form': form
    })

def deleteFile(request, slug):
    file = File.objects.get(slug=slug)
    file.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
