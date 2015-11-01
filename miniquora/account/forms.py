from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'dumb', 'placeholder' : 'Enter Password'}))
    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            self.user_cache = authenticate(username = username, password = password)
            if self.user_cache is None:
                raise forms.ValidationError('Invalid username or password')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('User is not Active')
        return self.cleaned_data

    def get_user(self):
        return self.user_cache

class SignupForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password1 = forms.CharField(label = 'Password', max_length = 20, widget = forms.PasswordInput())
    password2 = forms.CharField(label = 'Confirm Password',max_length = 20, widget = forms.PasswordInput())
    email = forms.EmailField(max_length = 254)
    phone_number = forms.CharField(max_length = 11)

    def clean_username(self):
        data_username = self.cleaned_data.get('username')
        if data_username and CustomUser.objects.count(username = data_username) > 0:
            raise forms.ValidationError('This username is already taken')
        return data_username



