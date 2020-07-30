'''accounts/views.py'''
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from accounts.forms import LoginForm, RegistrationForm


class LoginView(View):
    '''LoginView'''
    @classmethod
    def post(cls, request):
        '''post'''
        form = LoginForm(request.POST)
        if form.is_valid():
            cleande_data = form.cleaned_data
            user = authenticate(
                request,
                username=cleande_data['username'],
                password=cleande_data['password']
            )
            if user is None:
                return HttpResponse('Неправильный логин и/или пароль')

            if not user.is_active:
                return HttpResponse('Ваш аккаунт заблокирован')

            login(request, user)
            return HttpResponse('Добро пожаловать! Успешный вход')
        return render(request, 'accounts/login.html', {'form': form})

    @classmethod
    def get(cls, request):
        '''get'''
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def register(request):
    '''register'''
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            return render(request, "accounts/registration_complete.html",
                          {"new_user": new_user})
    else:
        form = RegistrationForm()

    return render(request, "accounts/register.html", {"user_form": form})
