from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, help_text="Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.", label='Имя пользователя', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password1 = forms.CharField(max_length=254, help_text="Ваш пароль должен содержать как минимум 8 символов.",label='Пароль', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(max_length=254, help_text="Повторите Ваш пароль.", label='Повтор пароля', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(max_length=254, help_text="Введите Ваш email.", label = "Email", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(max_length=254, help_text="Введите Ваше имя.", label='Имя', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=254, help_text="Введите Вашу фамилию.", label = 'Фамилия', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    
    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError('Пользователь с таким email уже зарегистрирован.')
        return email
    def clean_password2(self):
        if self.cleaned_data['password2'] != self.cleaned_data['password1']:
            raise ValidationError('Пароли не совпадают')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class ProfileSetForm(forms.ModelForm):
    study_group = forms.ChoiceField(label = 'Группа', widget=forms.Select(attrs={'class' : 'form-control'}),help_text = 'Выберите вашу группу', choices=((9413,9413),(943,943)))
    class Meta:
        model = Profile
        fields = ('study_group',)


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 150, label = 'Имя пользователя', widget=forms.TextInput(attrs={'class' : 'form-control fix-size'}))
    password = forms.CharField(max_length = 254, label = 'Пароль',  widget=forms.PasswordInput(attrs={'class' : 'form-control fix-size'}))