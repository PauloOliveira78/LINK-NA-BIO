from django.urls import path
from app import views

# Define as URLs do projeto
urlpatterns = [
    path('', views.index, name='index'),  # URL para a página inicial
    path('about/', views.about, name='about'),  # URL para a página sobre
    path('contact/', views.contact, name='contact'),  # URL para a página de contato
]
