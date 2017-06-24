from django.shortcuts import render,get_object_or_404,redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from accounts.models import UserProfile
from sparks.models import spark
from .forms import SearchForm,SuggestionForm
from sparks.forms import ContactForm
# Create your views here.

def homepage(request):
    return render(request,'accounts/home.html')

def malnutrition(request):
    sparks=spark.objects.order_by('spark_name')
    if request.user.is_authenticated:
        x=request.user.is_superuser
        if not x:
            userpro=UserProfile.objects.get(user=request.user)
        else:
            userpro=User.objects.get(username='malli')


    if request.method == 'GET':
        form = SuggestionForm()

    else:
        form = SuggestionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            if message is not None:
                try:
                    send_mail(subject+'-'+name, message, email, ['pvnmallikarjun@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return render(request,'sparks/success.html')

    if request.method == 'GET':
        form_one = SearchForm()
    else:
        form_one = SearchForm(request.POST)
        if form_one.is_valid():
            loc = form_one.cleaned_data.get('filter_locality')
            cit = form_one.cleaned_data.get('filter_city')
            top = form_one.cleaned_data.get('filter_topic')

            #sparks=spark.objects.filter()
            sparks=spark.objects.filter(spark_city__icontains=cit)
            sparks=sparks.filter(spark_locality__icontains=loc)


    # user = get_object_or_404(spark, pk=pk)
    # if request.method == 'GET':
    #     form_two = ContactForm()
    # else:
    #     form_two = ContactForm(request.POST)
    #     if form_two.is_valid():
    #         subject = form.cleaned_data.get('contact_name')
    #         from_email = form.cleaned_data.get('contact_email')
    #         topic = form.cleaned_data.get('topic')
    #         message = form.cleaned_data.get('content')

    #         if message is not None:
    #             try:
    #                 send_mail(topic+'-'+subject, message, from_email, [user.spark_mail])
    #             except BadHeaderError:
    #                 return HttpResponse('Invalid header found.')
    #             return redirect('sparks:success')
    if request.user.is_authenticated:
        return render(request,'accounts/malnutrition.html',{'sparks':sparks,'userpro':userpro,'form':form,'form_one':form_one})
    else:
        return render(request,'accounts/malnutrition.html',{'sparks':sparks,'form':form,'form_one':form_one})


def education(request):
    return render(request,'accounts/education.html')

def poverty(request):
    return render(request,'accounts/poverty.html')

def social(request):
    return render(request,'accounts/social.html')

def hygiene(request):
    return render(request,'accounts/hygiene.html')


def all_sparks(request):
    sparks=spark.objects.all()
    if request.method == 'GET':
        form = SearchForm()
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data.get('filter_locality')
            cit = form.cleaned_data.get('filter_city')
            top = form.cleaned_data.get('filter_topic')

            #sparks=spark.objects.filter()
            sparks=spark.objects.filter(spark_city__icontains=cit)
            sparks=sparks.filter(spark_locality__icontains=loc)
    return render(request,"sparks/all_sparks.html",{'sparks': sparks , 'form':form})