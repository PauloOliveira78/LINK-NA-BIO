import os
from pathlib import Path

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configurações de segurança
SECRET_KEY = 'sua-chave-secreta-gerada-aqui'  # Substitua por uma chave secreta gerada
DEBUG = True  # Defina como False em produção
ALLOWED_HOSTS = []  # Adicione os hosts permitidos em produção

# Configurações de aplicativos instalados
INSTALLED_APPS = [
    'django.contrib.admin',  # Aplicativo de administração do Django
    'django.contrib.auth',  # Aplicativo de autenticação do Django
    'django.contrib.contenttypes',  # Aplicativo de tipos de conteúdo do Django
    'django.contrib.sessions',  # Aplicativo de sessões do Django
    'django.contrib.messages',  # Aplicativo de mensagens do Django
    'django.contrib.staticfiles',  # Aplicativo de arquivos estáticos do Django
    'app',  # Adicione seu aplicativo aqui
]

# Configurações de middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Middleware de segurança
    'django.contrib.sessions.middleware.SessionMiddleware',  # Middleware de sessões
    'django.middleware.common.CommonMiddleware',  # Middleware comum
    'django.middleware.csrf.CsrfViewMiddleware',  # Middleware de proteção CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Middleware de autenticação
    'django.contrib.messages.middleware.MessageMiddleware',  # Middleware de mensagens
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Middleware de proteção contra clickjacking
]

# Configurações de URLs
ROOT_URLCONF = 'config.urls'

# Configurações de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Backend de templates do Django
        'DIRS': [BASE_DIR / '../frontend/templates'],  # Diretórios de templates
        'APP_DIRS': True,  # Habilita a busca de templates nos diretórios dos aplicativos
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Processador de contexto de debug
                'django.template.context_processors.request',  # Processador de contexto de request
                'django.contrib.auth.context_processors.auth',  # Processador de contexto de autenticação
                'django.contrib.messages.context_processors.messages',  # Processador de contexto de mensagens
            ],
        },
    },
]

# Configurações de WSGI
WSGI_APPLICATION = 'config.wsgi.application'

# Configurações de banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Backend de banco de dados SQLite
        'NAME': BASE_DIR / 'db.sqlite3',  # Nome do banco de dados
    }
}

# Configurações de autenticação
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Validador de similaridade de atributos do usuário
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Validador de comprimento mínimo da senha
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Validador de senha comum
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Validador de senha numérica
    },
]

# Configurações de internacionalização
LANGUAGE_CODE = 'pt-br'  # Código de idioma
TIME_ZONE = 'America/Sao_Paulo'  # Fuso horário
USE_I18N = True  # Habilita a internacionalização
USE_L10N = True  # Habilita a formatação local
USE_TZ = True  # Habilita o uso de fuso horário

# Configurações de arquivos estáticos
STATIC_URL = '/static/'  # URL para arquivos estáticos
STATICFILES_DIRS = [BASE_DIR / '../frontend/static']  # Diretórios de arquivos estáticos

# Configurações de e-mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Backend de e-mail SMTP
EMAIL_HOST = 'smtp.gmail.com'  # Host do servidor de e-mail
EMAIL_PORT = 587  # Porta do servidor de e-mail
EMAIL_USE_TLS = True  # Habilita TLS
EMAIL_HOST_USER = 'seu-email@gmail.com'  # Substitua pelo seu endereço de e-mail
EMAIL_HOST_PASSWORD = 'sua-senha'  # Substitua pela sua senha de e-mail

# Configurações de log
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'debug.log',  # Arquivo de log
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
