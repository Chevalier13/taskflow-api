from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-p2-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks', 
]

# 1. MIDDLEWARES CORRIGIDOS (Na ordem exata que o Django exige)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Exigido pelo erro E410
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Exigido pelo erro E408
    'django.contrib.messages.middleware.MessageMiddleware',      # Exigido pelo erro E409
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 2. BLOCO DE TEMPLATES ADICIONADO (Resolve o erro E403)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taskflow',
        'USER': 'admin',
        'PASSWORD': 'senha_secreta_123',
        'HOST': 'database',
        'PORT': '5432',
    }
}

ROOT_URLCONF = 'src.setup.urls'
WSGI_APPLICATION = 'src.setup.wsgi.application'
USE_TZ = True
STATIC_URL = 'static/'

# 3. LINHA ADICIONADA (Resolve o WARNING do terminal)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'