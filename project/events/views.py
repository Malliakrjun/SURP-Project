from django.shortcuts import render, redirect,get_object_or_404
from .forms import SubscriptionForm
from django.utils import timezone
# from django.contrib.auth.decorators import user_passes_test

from .forms import EventForm
from django.utils import timezone
from .models import event
from django.contrib.auth.models import User

# @user_passes_test(lambda x: x.is_superuser)
def add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            now = timezone.now()
            post.incomplete = post.event_time>=now
            post.save()
            form.save_m2m()
            return render(request,'events/event_display.html')
    else:
        form = EventForm()

    return render(request, 'events/event_form.html', {'form': form,})

def attend(request,pk,pk2):
    user = get_object_or_404(User, pk=pk)
    eventa = get_object_or_404(event, pk=pk2)
    eventa.interested_users.add(user)
    return render(request,'sparks/success.html')

def not_attending(request,pk,pk2):
    user = get_object_or_404(User, pk=pk)
    eventa = get_object_or_404(event, pk=pk2)
    eventa.interested_users.remove(user)
    return render(request,'sparks/success.html')

def events(request):
    if request.method == 'GET':
        form = SubscriptionForm()
    else:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscribers=[]
            s_email = form.cleaned_data.get('subscriber_email')
            subscribers.append(s_email)
            return redirect('/events/')

    events_left = []
    events_completed = []
    events=event.objects.all()
    for eventi in events:
        if eventi.event_time > timezone.now():
            events_left.append(eventi)
        else:
            events_completed.append(eventi)

    user=request.user
    userevents=user.event_set.all()
    return render(request,'events/event_display.html',{'events':events_left,'completed_events':events_completed,'userevents':userevents,'form': form})
