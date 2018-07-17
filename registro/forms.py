from django.forms import ModelForm
from .models import Registro
from servicio.models import Servicio

class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields = ['servicio', 'reg_user', 'reg_pass']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['servicio'].queryset = Servicio.objects.filter(owner = user)

