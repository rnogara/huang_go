from django.shortcuts import render
from datetime import date
from .models import Events
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from .forms import ContactForm


def home(request):
    message = None
    if request.method == "POST":
        name = request.POST["nome"]
        from_email = request.POST["email"]
        message = request.POST["mensagem"]
        subject = 'Contato do site Hung Go'
        if subject and message and from_email:
            try:
                send_mail(subject, message + f'\n enviado por: {name}\nemail: {from_email}', from_email=from_email, recipient_list=[settings.EMAIL_HOST_USER,])
            except BadHeaderError:
                message = "Invalid header found."
            message = "Email enviado com sucesso!"
        else:
            message = "Tenha certeza que todos os campos estão preenchidos e tente novamente."


    def toggleHideBtn(e):
        e.classList.toggle("hide")
        e.parentElement.children[1].classList.toggle("hide")


    def toggleHideCard(e):
        e.classList.toggle("hide")
        e.parentElement.children[0].classList.toggle("hide")


    context = {"events": Events.objects.filter(date__gte=date.today())[:4],
               "form": ContactForm(), "toggleHideBtn": toggleHideBtn,
               "toggleHideCard": toggleHideCard, "message": message}
    
    return render(request, "home.html", context)