from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Rutas para productos
    path('', views.product_list, name='product_list'),
    path('trash/', views.product_trash, name='product_trash'), 
    path('create/', views.product_create, name='product_create'),
    path('edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('delete/permanently/<int:pk>/', views.product_delete_permanently, name='product_delete_permanently'),
    path('restore/<int:pk>/', views.product_restore, name='product_restore'),
    
    # Rutas para categorías
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
]
