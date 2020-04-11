from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, help_text="Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.", label='Имя пользователя')
    password1 = forms.CharField(max_length=254, help_text="Ваш пароль должен содержать как минимум 8 символов.", widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(max_length=254, help_text="Повторите Ваш пароль.", widget=forms.PasswordInput, label='Повтор пароля')
    email = forms.EmailField(max_length=254, help_text="Введите Ваш email.", label = "Email")
    first_name = forms.CharField(max_length=254, help_text="Введите Ваше имя.", label='Имя')
    last_name = forms.CharField(max_length=254, help_text="Введите Вашу фамилию.", label = 'Фамилия')
    
    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError('Пользователь с таким email уже зарегистрирован.')
        return email

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class ProfileSetForm(forms.ModelForm):
    study_group = forms.ChoiceField(label = 'Группа',help_text = 'Выберите вашу группу', choices=((9413,9413),(943,943)))
    class Meta:
        model = Profile
        fields = ('study_group',)


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 150, label = 'Имя пользователя')
    password = forms.CharField(max_length = 254, label = 'Пароль', widget=forms.PasswordInput)