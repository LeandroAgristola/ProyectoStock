from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [   
    # URLs para Vendedores
    path('vendedores/', views.vendedor_list, name='vendedor_list'),
    path('vendedores/nuevo/', views.vendedor_create, name='vendedor_create'),
    path('vendedores/<int:pk>/editar/', views.vendedor_edit, name='vendedor_edit'),
    path('vendedores/<int:pk>/detalle/', views.vendedor_detail, name='vendedor_detail'),

    # URLs para Choferes
    path('choferes/', views.chofer_list, name='chofer_list'),
    path('choferes/nuevo/', views.chofer_create, name='chofer_create'),
    path('choferes/<int:pk>/editar/', views.chofer_edit, name='chofer_edit'),
    path('choferes/<int:pk>/detalle/', views.chofer_detail, name='chofer_detail'),
    
    # URLs para acciones genéricas
    path('<str:tipo>/<int:pk>/desactivar/', views.desactivar_staff, name='desactivar_staff'),
    path('<str:tipo>/<int:pk>/reactivar/', views.reactivar_staff, name='reactivar_staff'),
    path('<str:tipo>/<int:pk>/eliminar/', views.eliminar_staff, name='eliminar_staff'),
]