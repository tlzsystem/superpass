from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Servicio
from django.urls import reverse_lazy

class ServicioList(ListView):
    def get_queryset(self):
        return Servicio.objects.filter(owner= self.request.user, active=True)

class ServicioCreate(CreateView):
    model = Servicio
    fields = ['name','url']
    success_url = reverse_lazy('servicio-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ServicioUpdate(UpdateView):
    model = Servicio
    fields = ['name','url']
    success_url = reverse_lazy('servicio-list')

class ServicioDelete(DeleteView):
    model = Servicio
    success_url = reverse_lazy('servicio-list')

