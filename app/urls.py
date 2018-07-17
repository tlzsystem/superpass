"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from servicio.views import ServicioList, ServicioCreate, ServicioUpdate, ServicioDelete
from registro.views import RegistroList, RegistroCreate, RegistroUpdate, RegistroDelete
from dashboard.views import DahsboardView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(DahsboardView.as_view()),name='dashboard-view'),
    path('servicios/', login_required(ServicioList.as_view()),name='servicio-list'),
    path('servicios/add/', login_required(ServicioCreate.as_view()),name='servicio-create'),
    path('servicios/<int:pk>/', login_required(ServicioUpdate.as_view()),name='servicio-update'),
    path('servicios/delete/<int:pk>/', login_required(ServicioDelete.as_view()),name='servicio-delete'),
    path('registros/', login_required(RegistroList.as_view()),name='registro-list'),
    path('registros/add/', login_required(RegistroCreate.as_view()),name='registro-create'),
    path('registros/<int:pk>/', login_required(RegistroUpdate.as_view()),name='registro-update'),
    path('registros/delete/<int:pk>/', login_required(RegistroDelete.as_view()),name='registro-delete'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
