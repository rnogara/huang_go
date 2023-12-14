from django.shortcuts import render
from datetime import date
from .models import Events
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm


def home(request):
    if request.method == "POST":
        name = request.POST["name"]
        from_email = request.POST["email"]
        message = request.POST["message"]
        subject = 'Contato do site'
        if subject and message and from_email:
            try:
                send_mail(subject, message + f'\n enviado por: {name}', from_email, ['tonyjjh@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return HttpResponseRedirect("/contact/thanks/")
        else:
            return HttpResponse("Make sure all fields are entered and valid.")

    context = {"events": Events.objects.filter(date__gte=date.today()), "form": ContactForm()}
    return render(request, "home.html", context)