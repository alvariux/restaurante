import django.forms as forms
from .models import Mesa, MesaEstado, Orden

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

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['mesa', 'empleado']
        widgets = {
            'mesa': forms.Select(attrs={'class': 'form-control'}),
            'empleado': forms.HiddenInput(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        orden = super().save(commit=False)
        if commit:
            orden.estatus = 'pendiente'  # Set default status
            orden.empleado = self.initial['empleado']
            orden.save()
        return orden