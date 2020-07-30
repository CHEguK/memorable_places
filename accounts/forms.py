''' accounts/forms.py '''
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    ''' Login Form '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    ''' Registration Form '''
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        ''' Meta '''
        model = User
        fields = ("username", "email", "first_name")
        labels = {"username": 'Логин', "email": 'Email', "first_name": 'Имя'}

        def clean_password2(self) -> str:
            ''' Check password are the same '''
            clean_data = self.cleaned_data  # pylint: disable=no-member
            if clean_data["password"] != clean_data["password2"]:
                raise forms.ValidationError("Пароли не совпадают")
            return clean_data["password2"]
