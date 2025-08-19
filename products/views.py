from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Product, Category
from .forms import ProductForm, CategoryForm


@login_required
def product_list(request):
    """
    Vista que lista productos activos con filtros.
    - Filtra por categoría, estado de stock y búsqueda por nombre/código.
    - Renderiza el template de productos disponibles.
    """
    # Obtener parámetros de filtrado
    category_filter = request.GET.get('category')
    status_filter = request.GET.get('status')
    search_query = request.GET.get('search')

    # QuerySet base para todos los productos disponibles
    products = Product.objects.filter(available=True)

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
        products = products.filter(stock__exact=0)
    
    context = {
        'products': products,
        'categories': Category.objects.all(),
        'filters': {
            'category': category_filter,
            'status': status_filter,
            'search': search_query,
        },
        'active_tab': 'available', # Indica qué pestaña está activa
    }
    return render(request, 'products/product_list.html', context)


@login_required
def product_trash(request):
    """
    Vista que muestra los productos en la papelera (no disponibles).
    """
    inactive_products = Product.objects.filter(available=False)
    
    context = {
        'inactive_products': inactive_products,
        'active_tab': 'trash', # Indica qué pestaña está activa
    }
    return render(request, 'products/product_trash.html', context)


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
        'title': 'Nuevo Producto',
        'active_tab': 'create', # Indica qué pestaña está activa
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
        'title': 'Editar Producto',
        'active_tab': 'available', # La pestaña activa al editar es 'Disponibles'
    }
    return render(request, 'products/product_form.html', context)


@login_required
def product_delete(request, pk):
    """
    Vista para mover un producto a la papelera (lo marca como no disponible).
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        # La lógica de eliminación está en la vista. Se mantiene POST para mayor seguridad.
        pass # La lógica se manejará con el enlace del template
    
    product.available = False
    product.save()
    messages.success(request, "Producto movido a la papelera.")
    return redirect('products:product_list')


@login_required
def product_delete_permanently(request, pk):
    """
    Vista para eliminar un producto de forma permanente.
    """
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, "Producto eliminado permanentemente.")
    return redirect('products:product_trash')


@login_required
def product_restore(request, pk):
    """
    Vista para restaurar un producto de la papelera.
    """
    product = get_object_or_404(Product, pk=pk)
    product.available = True
    product.save()
    messages.success(request, "Producto restaurado exitosamente.")
    return redirect('products:product_trash')


@login_required
def category_list(request):
    """
    Vista que lista las categorías.
    """
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'active_tab': 'categories', # Indica qué pestaña está activa
    }
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
        'title': 'Nueva Categoría',
        'active_tab': 'categories', # La pestaña activa al crear es 'Categorías'
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
        'title': 'Editar Categoría',
        'active_tab': 'categories', # La pestaña activa al editar es 'Categorías'
    }
    return render(request, 'products/category_form.html', context)


@login_required
def category_delete(request, pk):
    """
    Vista para eliminar una categoría.
    """
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, f"Categoría eliminada exitosamente.")
    return redirect('products:category_list')
