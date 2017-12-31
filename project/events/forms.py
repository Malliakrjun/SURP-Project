from django import forms
# from django.utils.text import slugify
from datetime import datetime
from .models import event
from django.utils import timezone

class EventForm(forms.ModelForm):
    class Meta:
        model = event
        fields = (
            'event_title',
            'event_time',
            'description',
            'venue',
            'image',

        )


class SubscriptionForm(forms.Form):
    subscriber_email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class' : 'w3-input w3-border','placeholder':'Your Email'}))

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields['subscriber_email'].label = ""


    # def save(self):
    #     if self.instance.pk:
    #         return super(AddForm, self).save()
    #     instance = super(EventForm, self).save(commit=False)
    #     now = timezone.now()
    #     instance.incomplete = instance.event_time>=now
    #     instance.save()

    #     return instance