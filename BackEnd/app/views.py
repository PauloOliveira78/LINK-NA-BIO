from django.shortcuts import render

# View para a página inicial
def index(request):
    return render(request, 'index.html')

# View para a página sobre
def about(request):
    return render(request, 'about.html')

# View para a página de contato
def contact(request):
    return render(request, 'contact.html')
