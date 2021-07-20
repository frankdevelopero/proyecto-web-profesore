from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(label="Correo electrónico", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'type': 'email'
        }
    ))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'type': 'password',
            'id': 'password_login'
        }
    ))


class RegisterForm(forms.Form):
    firstname = forms.CharField(label="nombres", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
        }
    ))

    lastname = forms.CharField(label="apellidos", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
        }
    ))

    phone = forms.IntegerField(label="Nro de celular", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
        }
    ))

    email = forms.EmailField(label="Correo electrónico", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'type': 'email'
        }
    ))

    password = forms.CharField(label="contraseña", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'type': 'password',
            'id': 'password_register'
        }
    ))