from django import forms

# class contactForm(forms.ModelForm):

#     class Meta():
#         model = contact
#         fields = ('your_name','name_of_your_organisation','your_email','your_info','subject','message',)


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class' : 'w3-input w3-border','placeholder':'Your Name'}))
    contact_email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class' : 'w3-input w3-border','placeholder':'Your Email'}))
    topic = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class' : 'w3-input w3-border','placeholder':'Subject'}),
    )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class' : 'w3-input w3-border','placeholder':'Message'}),
    )


    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = ""
        self.fields['contact_email'].label = ""
        self.fields['topic'].label = ""
        self.fields['content'].label = ""






