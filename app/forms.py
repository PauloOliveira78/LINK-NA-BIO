from django import forms

# Formulário de contato
class MyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)  # Campo de nome
    email = forms.EmailField(label='Email')  # Campo de e-mail
    message = forms.CharField(label='Message', widget=forms.Textarea)  # Campo de mensagem