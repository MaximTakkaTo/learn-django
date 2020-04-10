from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, ProfileSetForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login
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
                
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username = username, password = password)
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