from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def home(request):
    return JsonResponse({"status": "API Taskflow Rodando com Sucesso", "banco": "Postgres Conectado"})

urlpatterns = [
    path('', home),  # Rota raiz para o localhost parar de dar erro
    path('admin/', admin.site.urls),
]