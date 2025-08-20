from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from django.http import JsonResponse


@login_required
def product_list(request):
    category_filter = request.GET.get('category')
    status_filter = request.GET.get('status')
    search_query = request.GET.get('search') or ''  # <- evita "None"

    products = Product.objects.filter(available=True)
    if search_query:
        products = products.filter(Q(name__icontains=search_query) | Q(code__icontains=search_query))
    if category_filter:
        products = products.filter(category_id=category_filter)
    if status_filter == 'in_stock':
        products = products.filter(stock__gt=0)
    elif status_filter == 'out_of_stock':
        products = products.filter(stock__exact=0)

    context = {
        'products': products,
        'categories': Category.objects.all(),
        'filters': {'category': category_filter, 'status': status_filter, 'search': search_query},
        'active_tab': 'available',
    }
    return render(request, 'products/product_list.html', context)

@login_required
def subcategories_api(request):
    parent_id = request.GET.get('parent')
    qs = Category.objects.filter(parent_id=parent_id).values('id', 'name') if parent_id else []
    return JsonResponse({'results': list(qs)})


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
            product = form.save(commit=False)
            product.available = True
            product.save()
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
            product = form.save(commit=False)
            if not product.available:
                product.available = True
            product.save()
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
    product = get_object_or_404(Product, pk=pk)
    if request.method != 'POST':
        messages.error(request, "Acción inválida.")
        return redirect('products:product_list')
    product.available = False
    product.save()
    messages.success(request, "Producto movido a la papelera.")
    return redirect('products:product_list')

@login_required
def product_restore(request, pk):
    if request.method != 'POST':
        messages.error(request, "Acción inválida.")
        return redirect('products:product_trash')
    product = get_object_or_404(Product, pk=pk)
    product.available = True
    product.save()
    messages.success(request, "Producto restaurado exitosamente.")
    return redirect('products:product_trash')

@login_required
def product_delete_permanently(request, pk):
    if request.method != 'POST':
        messages.error(request, "Acción inválida.")
        return redirect('products:product_trash')
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, "Producto eliminado permanentemente.")
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
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            # Subcategorías nuevas
            for name in request.POST.getlist('subcategories'):
                if name.strip():
                    Category.objects.create(name=name.strip(), parent=category)
            messages.success(request, "Categoría creada con éxito.")
            return redirect('products:category_list')
    else:
        form = CategoryForm()
    return render(request, 'products/category_form.html', {'form': form, 'title': 'Nueva Categoría'})


@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            # nuevas subcategorías
            for name in request.POST.getlist('subcategories'):
                if name.strip():
                    Category.objects.create(name=name.strip(), parent=category)
            # eliminar subcategorías
            ids_remove = request.POST.getlist('remove_children')
            if ids_remove:
                Category.objects.filter(id__in=ids_remove, parent=category).delete()
            messages.success(request, "Categoría actualizada.")
            return redirect('products:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'products/category_form.html', {'form': form, 'title': 'Editar Categoría'})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method != 'POST':
        messages.error(request, "Acción inválida.")
        return redirect('products:category_list')
    category.delete()
    messages.success(request, "Categoría eliminada exitosamente.")
    return redirect('products:category_list')
