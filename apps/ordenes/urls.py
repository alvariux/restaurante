from django.urls import path
from . import views

app_name = 'ordenes'

urlpatterns = [
    path('mesas_estado/', views.MesaEstadoListView.as_view(), name='mesas_estado_list'),
    path('mesas_estado/nuevo/', views.MesaEstadoCreateView.as_view(), name='mesas_estado_create'),
    path('mesas_estado/editar/<int:pk>/', views.MesaEstadoUpdateView.as_view(), name='mesas_estado_update'),
    path('mesas_estado/eliminar/<int:pk>/', views.MesaEstadoDeleteView.as_view(), name='mesas_estado_delete'),
    path('mesas/', views.MesaListView.as_view(), name='mesas_list'),
    path('mesas/nuevo/', views.MesaCreateView.as_view(), name='mesas_create'),
    path('mesas/editar/<int:pk>/', views.MesaUpdateView.as_view(), name='mesas_update'),
    path('mesas/eliminar/<int:pk>/', views.MesaDeleteView.as_view(), name='mesas_delete'),
]