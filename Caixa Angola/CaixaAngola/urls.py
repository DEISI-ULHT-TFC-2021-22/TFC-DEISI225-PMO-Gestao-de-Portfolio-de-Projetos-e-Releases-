"""CaixaAngola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from main import views
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('NovasOportunidades', views.novasoportunidades, name='NovasOportunidades'),
    
    path('Propostas', views.propostas, name='Propostas'),
    path('aprovar/<oportunidade_id>', views.approve_oportunidade, name='approve_oportunidade'),
    path('editar/<oportunidade_id>', views.edit_oportunidade, name='edit_oportunidade'),
    path('deletar/<oportunidade_id>', views.delete_oportunidade, name='delete_oportunidade'),
    path('oportunidade/<oportunidade_id>/', views.oportunidade_details, name='oportunidade-details'),
    path('Status', views.status, name='Status'),
    path('Status/<oportunidade_id>', views.status_oportunidade, name='status_oportunidade'),

    path('status_search', views.status_search, name='status_search'),
    path('submission_status_search', views.submission_status_search, name='submission_status_search'),
    path('propostas_search', views.propostas_search, name='propostas_search'),

    path('SubmissionStatus', views.submissionstatus, name='submissionStatus'),
    path('CaixaSocial', views.caixasocial, name='caixaSocial'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('indexPMO', views.indexpmo, name='indexPMO'),
    path('indexGestor', views.indexgestor, name='indexGestor'),
    # path('Manual', views.manual, name='manual'),
    path('', include('notes.urls')),
    path('AddEvent', views.addevent, name='addevent'),
    path('edit/<event_id>', views.edit_event, name='edit_event'),
    path('delete/<event_id>', views.delete_event, name='delete_event'),
    path('EventList', views.eventlist, name='eventlist'),
    
    path('AddDocument', views.adddocument, name='adddocument'),
    path('editar/<document_id>', views.edit_document, name='edit_document'),
    path('apagar/<document_id>', views.delete_document, name='delete_document'),
    path('DocumentList', views.documentlist, name='documentlist'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
