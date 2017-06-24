from django.shortcuts import render,get_object_or_404,redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import spark
from .forms import ContactForm

# Create your views here.



# def contact_form(request,pk):
#     spark_obj = get_object_or_404(spark, pk=pk)
#     if request.method == "POST":
#         form = contactForm(request.POST, instance=post)
#         if form.is_valid():
#             spark_obj = form.save(commit=False)
#             spark_obj.author = request.user
#             spark_obj.published_date = timezone.now()
#             spark_obj.save()
#             return redirect('blog:post_detail', pk=post.pk)
#     else:
#         form = contactForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})



# def contact(request,pk):
#     form_class = ContactForm

#     # new logic!
#     if request.method == 'POST':
#         form = form_class(data=request.POST)

#         if form.is_valid():
#             contact_name = request.POST.get(
#                 'contact_name'
#             , '')
#             contact_email = request.POST.get(
#                 'contact_email'
#             , '')
#             form_content = request.POST.get('content', '')

#             # Email the profile with the
#             # contact information
#             template = get_template('contact_template.txt')
#             context = Context({
#                 'contact_name': contact_name,
#                 'contact_email': contact_email,
#                 'form_content': form_content,
#             })
#             content = template.render(context)

#             email = EmailMessage(
#                 "New contact form submission",
#                 content,
#                 "Your website" +'',
#                 ['youremail@gmail.com'],
#                 headers = {'Reply-To': contact_email }
#             )
#             email.send()
#             return redirect('contact')

#     return render(request, 'sparks/contact.html', {
#         'form': form_class,
#     })


def profile(request,pk):
    user = get_object_or_404(spark, pk=pk)
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('contact_name')
            from_email = form.cleaned_data.get('contact_email')
            topic = form.cleaned_data.get('topic')
            message = form.cleaned_data.get('content')

            if message is not None:
                try:
                    send_mail(topic+'-'+subject, message, from_email, [user.spark_mail])        #change this later
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('sparks:success')
    return render(request, "sparks/contact.html", {'form': form , 'spark':user})


def success(request):
    return HttpResponse('Success! Thank you for your message.')
