import django.forms as forms
from .models import Mesa, MesaEstado

class MesaEstadoForm(forms.ModelForm):
    class Meta:
        model = MesaEstado
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['nombre', 'capacidad', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'})
        }