from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from accounts.models import UserProfile
# class contactForm(forms.ModelForm):

#     class Meta():
#         model = contact
#         fields = ('your_name','name_of_your_organisation','your_email','your_info','subject','message',)


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class' : 'w3-input','placeholder':'Your Name'}))
    contact_email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class' : 'w3-input','placeholder':'Your Email'}))
    topic = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class' : 'w3-input','placeholder':'Subject'}),
    )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class' : 'w3-input','placeholder':'Message'}),
    )


    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = ""
        self.fields['contact_email'].label = ""
        self.fields['topic'].label = ""
        self.fields['content'].label = ""


class SparkForm(UserCreationForm):
    first_name=forms.CharField(max_length=150)
    last_name=forms.CharField(max_length=150)
    email=forms.EmailField(required=True)

    class meta():
        model=UserProfile
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





