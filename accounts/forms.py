from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "first_name")
        labels = {"username": 'Логин', "email": 'Пароль', "first_name": 'Имя'}

        def clean_password2(self):
            cd = self.cleaned_data
            if cd["password"] != cd["password2"]:
                raise forms.ValidationError("Пароли не совпадают")
            return cd["password2"]