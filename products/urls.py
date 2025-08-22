from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('trash/', views.product_trash, name='product_trash'),
    path('new/', views.product_create, name='product_create'),
    path('<int:pk>/edit/', views.product_edit, name='product_edit'),

    # Acciones por POST
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('<int:pk>/restore/', views.product_restore, name='product_restore'),
    path('<int:pk>/delete-permanently/', views.product_delete_permanently, name='product_delete_permanently'),

    # Categorías
    path('categories/', views.category_list, name='category_list'),
    path('categories/new/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # API subcategorías
    path('api/subcategories/', views.subcategories_api, name='subcategories_api'),

    # Combos
    path('combos/', views.combo_list, name='combo_list'),
    path('combos/new/', views.combo_create, name='combo_create'),
    path('combos/<int:pk>/edit/', views.combo_edit, name='combo_edit'),
    path('combos/<int:pk>/delete/', views.combo_delete, name='combo_delete'),
]