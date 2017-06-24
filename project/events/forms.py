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

    # def save(self):
    #     if self.instance.pk:
    #         return super(AddForm, self).save()
    #     instance = super(EventForm, self).save(commit=False)
    #     now = timezone.now()
    #     instance.incomplete = instance.event_time>=now
    #     instance.save()

    #     return instance