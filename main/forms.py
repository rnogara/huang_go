from django import forms


class EventForm(forms.Form):
    title = forms.CharField(max_length=200)
    type = forms.CharField(max_length=100)
    date = forms.DateField()
    location = forms.CharField(max_length=200)


class ContactForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)