from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.utils.translation import gettext as _

class RegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=150)
    last_name=forms.CharField(max_length=150)
    email=forms.EmailField(required=True)

    class meta():
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            )
    def save(self,commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']

        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):

    class meta():
        model=User
        fields=(
                'email',
                'first_name',
                'last_name',
                'password',
            )

        #exclude='__all__'

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class' : 'w3-input w3-border','placeholder':'USERNAME'}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'class' : 'w3-input w3-border','placeholder':'PASSWORD'}))
