from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Product, Category
from .forms import ProductForm, CategoryForm

@login_required
def product_list(request):
    """
    Vista que lista productos con filtros.
    - Filtra por categoría, estado de stock y búsqueda por nombre/código.
    - Separa productos activos (disponibles) e inactivos (en papelera).
    """
    # Obtener parámetros de filtrado
    category_filter = request.GET.get('category')
    status_filter = request.GET.get('status')
    search_query = request.GET.get('search')

    # QuerySet base para todos los productos disponibles
    products = Product.objects.filter(available=True)

    # QuerySet para los productos en papelera
    inactive_products = Product.objects.filter(available=False)

    # Aplicar filtros de búsqueda
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | Q(code__icontains=search_query)
        )

    if category_filter:
        products = products.filter(category_id=category_filter)

    # Aplicar filtro de stock
    if status_filter == 'in_stock':
        products = products.filter(stock__gt=0)
    elif status_filter == 'out_of_stock':
        products = products.filter(stock=0)

    # Obtener todas las categorías para el filtro del sidebar
    categories = Category.objects.all()
    
    # Preparar el contexto para la plantilla
    context = {
        'active_products': products,  # Usar el nombre de variable correcto
        'inactive_products': inactive_products, # Usar el nombre de variable correcto
        'categories': categories,
        'filters': {
            'category': category_filter,
            'status': status_filter,
            'search': search_query,
        }
    }

    return render(request, 'products/product_list.html', context)

@login_required
def product_create(request):
    """
    Vista para crear un nuevo producto.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado exitosamente.")
            return redirect('products:product_list')
    else:
        form = ProductForm()
    
    context = {
        'form': form,
        'title': 'Nuevo Producto'
    }
    return render(request, 'products/product_form.html', context)


@login_required
def product_edit(request, pk):
    """
    Vista para editar un producto existente.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado exitosamente.")
            return redirect('products:product_list')
    else:
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'title': 'Editar Producto'
    }
    return render(request, 'products/product_form.html', context)


@login_required
def product_delete(request, pk):
    """
    Vista para 'eliminar' un producto (enviar a la papelera).
    """
    product = get_object_or_404(Product, pk=pk)
    product.delete()  # Llama al método sobrescrito en el modelo
    messages.success(request, f"Producto '{product.name}' enviado a la papelera.")
    return redirect('products:product_list')


@login_required
def product_restore(request, pk):
    """
    Vista para restaurar un producto de la papelera.
    """
    product = get_object_or_404(Product, pk=pk, active=False)
    product.active = True
    product.deleted_at = None
    product.save()
    messages.success(request, f"Producto '{product.name}' restaurado exitosamente.")
    return redirect('products:product_list')


@login_required
def product_delete_permanently(request, pk):
    """
    Vista para eliminar un producto de forma permanente.
    """
    product = get_object_or_404(Product, pk=pk, active=False)
    product_name = product.name
    product.delete(hard=True) # Eliminación definitiva, sin pasar por la sobrescritura del delete()
    messages.success(request, f"Producto '{product_name}' eliminado permanentemente.")
    return redirect('products:product_list')


@login_required
def category_list(request):
    """
    Vista para listar, editar y eliminar categorías.
    """
    categories = Category.objects.filter(parent__isnull=True).prefetch_related('subcategories')
    context = {'categories': categories}
    return render(request, 'products/category_list.html', context)


@login_required
def category_create(request):
    """
    Vista para crear una nueva categoría.
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría creada exitosamente.")
            return redirect('products:category_list')
    else:
        form = CategoryForm()
    
    context = {
        'form': form,
        'title': 'Nueva Categoría'
    }
    return render(request, 'products/category_form.html', context)


@login_required
def category_edit(request, pk):
    """
    Vista para editar una categoría existente.
    """
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría actualizada exitosamente.")
            return redirect('products:category_list')
    else:
        form = CategoryForm(instance=category)
    
    context = {
        'form': form,
        'title': 'Editar Categoría'
    }
    return render(request, 'products/category_form.html', context)


@login_required
def category_delete(request, pk):
    """
    Vista para eliminar una categoría.
    """
    category = get_object_or_404(Category, pk=pk)
    category_name = category.name

    # Al eliminar una categoría, los productos asociados a ella se quedan sin categoría
    # debido a la propiedad on_delete=models.SET_NULL en el modelo Product.
    # Al eliminar una categoría padre, las subcategorías se convierten en categorías de nivel superior
    # debido a la propiedad on_delete=models.SET_NULL en el modelo Category.
    category.delete()
    messages.success(request, f"Categoría '{category_name}' eliminada exitosamente.")
    return redirect('products:category_list')