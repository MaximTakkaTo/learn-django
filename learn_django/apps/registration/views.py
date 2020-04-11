from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import SignUpForm, ProfileSetForm, LoginForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            profile_form = ProfileSetForm(request.POST)
            if form.is_valid() and profile_form.is_valid():
                user = form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                user.is_active = False
                un = form.cleaned_data.get('username')
                pw = form.cleaned_data.get('password1')
                profile.SendVerify()
                user = authenticate(username = un, password = pw)
                login(request, user)
                return HttpResponseRedirect(reverse('modules:modules'))
            else:
                return render(request, 'registration/signup.html', {'form': form, 'profile_form': profile_form})
        else:
            form = SignUpForm()
            pofile_form = ProfileSetForm()
            return render(request, 'registration/signup.html', {'form': form, 'profile_form': pofile_form})
    else:
        return HttpResponseRedirect(reverse('modules:modules'))

def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                un = form.cleaned_data.get('username')
                pw = form.cleaned_data.get('password')
                user = authenticate(username = un, password = pw)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('modules:modules'))
            return render(request, 'registration/signin.html', {'form': form, 'error' : 'Неверный логин или пароль'})
        else:
            form = LoginForm()
            return render(request, 'registration/signin.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('modules:modules'))

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse('registration:signin'))

def verify(request, uuid):
    try:
        profile = Profile.objects.get(uuid = uuid)
    except:
         return HttpResponseRedirect(reverse('registration:logout'))
    
    profile.user.is_active = True
    return HttpResponseRedirect(reverse('modules:modules'))