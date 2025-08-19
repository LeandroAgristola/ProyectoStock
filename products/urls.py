from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # URLs para productos
    path('', views.product_list, name='product_list'),
    path('crear/', views.product_create, name='product_create'),
    path('editar/<int:pk>/', views.product_edit, name='product_edit'),
    path('eliminar/<int:pk>/', views.product_delete, name='product_delete'),
    path('restaurar/<int:pk>/', views.product_restore, name='product_restore'),
    path('eliminar_definitivamente/<int:pk>/', views.product_delete_permanently, name='product_delete_permanently'),

    # URLs para categorías
    path('categorias/', views.category_list, name='category_list'),
    path('categorias/crear/', views.category_create, name='category_create'),
    path('categorias/editar/<int:pk>/', views.category_edit, name='category_edit'),
    path('categorias/eliminar/<int:pk>/', views.category_delete, name='category_delete'),
]
