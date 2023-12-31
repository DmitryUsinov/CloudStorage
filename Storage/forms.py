from django import forms
from .models import File, Discipline
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = ['title', 'info', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
        }

class FileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['discipline_id'].empty_label = 'Дисциплина не выбрана'
        

    class Meta:
        model = File
        fields = ['title', 'info', 'discipline_id', 'upload']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            
        }

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-input'}))
     
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'groups']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.TextInput(attrs={'class': 'form-input'}),
            'password2': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.TextInput(attrs={'class': 'form-input'}),
                    
        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))