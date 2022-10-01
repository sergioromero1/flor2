import re
from django import forms
from users.models import User

class SignUpForm(forms.Form):

    first_name = forms.CharField(min_length= 2, max_length=15)
    last_name = forms.CharField(min_length= 2, max_length=15)
    username = forms.CharField(min_length= 4, max_length=15)
    email = forms.CharField(min_length=6,max_length=50,widget = forms.EmailInput())
    password = forms.CharField(max_length=70 , widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70 , widget=forms.PasswordInput())

    def clean_username(self):
        """Username must be unique"""

        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El username ya existe')
        pattern = "^[A-Za-z0-9_]*$"
        valid = bool(re.match(pattern, username))
        if not valid:
            raise forms.ValidationError("El username solo puede contener letras A-z, numeros 0-9 y _")
        return username

    def clean_email(self):
        """email must be unique"""

        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('El email ya esta registrado')
        return email

    def clean(self):
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return data

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        user.save()