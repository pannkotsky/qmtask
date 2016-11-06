from django.contrib.auth import forms as auth_forms
from django import forms
from django.utils.translation import ugettext_lazy as _


class LoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': '',
                                      'class': 'form-control'}),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class RegisterForm(auth_forms.UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        strip=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    field_order = [
        'username',
        'email',
        'password1',
        'password2'
    ]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update(
            {'class': 'form-control'})
