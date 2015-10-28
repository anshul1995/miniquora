from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'dumb', 'placeholder' : 'Enter Password'}))
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username = username, password = password)
            if user is None:
                raise forms.ValidationError('Invalid username or password')
            elif not user.is_active:
                raise forms.ValidationError('User is not Active')
        return self.cleaned_data
    

                    





