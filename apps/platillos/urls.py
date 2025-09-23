from django.urls import path
from . import views

app_name = 'platillos'

urlpatterns = [    
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
]