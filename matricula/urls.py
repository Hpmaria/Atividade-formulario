"""
URL configuration for matricula project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib import admin
from django.urls import path
from aluno.views import cadastrar_aluno, listar_alunos

from django.urls import path, include
from aluno.views import listar_alunos  # ou cadastrar_aluno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_alunos, name='home'),  # Redireciona a URL base para a listagem de alunos
    path('cadastrar/', cadastrar_aluno, name='cadastrar_aluno'),
    path('alunos/', listar_alunos, name='listar_alunos'),
]
