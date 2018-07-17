from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Registro
from .forms import RegistroForm
from django.urls import reverse_lazy

class RegistroList(ListView):
    def get_queryset(self):
        return Registro.objects.filter(servicio__owner=self.request.user,servicio__active=True, active=True)

class RegistroCreate(CreateView):
    success_url = reverse_lazy('registro-list')
    form_class = RegistroForm
    template_name = 'registro/registro_form.html'

    def get_form_kwargs(self):
        kwargs = super(RegistroCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class RegistroUpdate(UpdateView):
    success_url = reverse_lazy('registro-list')
    form_class = RegistroForm
    template_name = 'registro/registro_form.html'
    def get_queryset(self):
        return Registro.objects.filter(servicio__owner=self.request.user,servicio__active=True, active=True)

    def get_form_kwargs(self):
        kwargs = super(RegistroUpdate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
class RegistroDelete(DeleteView):
    model = Registro
    success_url = reverse_lazy('registro-list')
