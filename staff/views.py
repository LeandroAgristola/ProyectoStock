from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Vendedor, Chofer
from .forms import VendedorForm, ChoferForm

# --- Vistas para Vendedores ---

@login_required
def vendedor_list(request):
    activos = Vendedor.objects.filter(activo=True)
    inactivos = Vendedor.objects.filter(activo=False)
    return render(request, 'staff/vendedor_list.html', {
        'vendedores_activos': activos,
        'vendedores_inactivos': inactivos,
        'active_tab': 'vendedores'
    })

@login_required
def vendedor_create(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff:vendedor_list')
    else:
        form = VendedorForm()
    return render(request, 'staff/staff_form.html', {
        'form': form,
        'title': 'Nuevo Vendedor',
        'active_tab': 'vendedores'
    })

@login_required
def vendedor_edit(request, pk):
    vendedor = get_object_or_404(Vendedor, pk=pk)
    if request.method == 'POST':
        form = VendedorForm(request.POST, instance=vendedor)
        if form.is_valid():
            form.save()
            return redirect('staff:vendedor_list')
    else:
        form = VendedorForm(instance=vendedor)
    return render(request, 'staff/staff_form.html', {
        'form': form,
        'title': 'Editar Vendedor',
        'active_tab': 'vendedores'
    })

@login_required
def vendedor_detail(request, pk):
    vendedor = get_object_or_404(Vendedor, pk=pk)
    # Aquí puedes añadir lógica para obtener ventas y métricas del vendedor
    return render(request, 'staff/staff_detail.html', {
        'staff': vendedor,
        'tipo': 'Vendedor',
        'active_tab': 'vendedores'
    })

# --- Vistas para Choferes ---

@login_required
def chofer_list(request):
    activos = Chofer.objects.filter(activo=True)
    inactivos = Chofer.objects.filter(activo=False)
    return render(request, 'staff/chofer_list.html', {
        'choferes_activos': activos,
        'choferes_inactivos': inactivos,
        'active_tab': 'choferes'
    })

@login_required
def chofer_create(request):
    if request.method == 'POST':
        form = ChoferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff:chofer_list')
    else:
        form = ChoferForm()
    return render(request, 'staff/staff_form.html', {
        'form': form,
        'title': 'Nuevo Chofer',
        'active_tab': 'choferes'
    })

@login_required
def chofer_edit(request, pk):
    chofer = get_object_or_404(Chofer, pk=pk)
    if request.method == 'POST':
        form = ChoferForm(request.POST, instance=chofer)
        if form.is_valid():
            form.save()
            return redirect('staff:chofer_list')
    else:
        form = ChoferForm(instance=chofer)
    return render(request, 'staff/staff_form.html', {
        'form': form,
        'title': 'Editar Chofer',
        'active_tab': 'choferes'
    })

@login_required
def chofer_detail(request, pk):
    chofer = get_object_or_404(Chofer, pk=pk)
    # Aquí puedes añadir lógica para obtener envíos realizados/pendientes
    return render(request, 'staff/staff_detail.html', {
        'staff': chofer,
        'tipo': 'Chofer',
        'active_tab': 'choferes'
    })

# --- Acciones (Desactivar, Reactivar, Eliminar) ---

@require_POST
@login_required
def desactivar_staff(request, tipo, pk):
    Model = Vendedor if tipo == 'vendedor' else Chofer
    staff = get_object_or_404(Model, pk=pk)
    
    fecha_baja = request.POST.get('fecha_baja')
    if fecha_baja:
        staff.fecha_baja = fecha_baja
        staff.activo = False
        staff.save()
        
    redirect_url = 'staff:vendedor_list' if tipo == 'vendedor' else 'staff:chofer_list'
    return redirect(redirect_url)

@require_POST
@login_required
def reactivar_staff(request, tipo, pk):
    Model = Vendedor if tipo == 'vendedor' else Chofer
    staff = get_object_or_404(Model, pk=pk)

    fecha_alta = request.POST.get('fecha_alta')
    if fecha_alta:
        staff.fecha_alta = fecha_alta
        staff.fecha_baja = None
        staff.activo = True
        staff.save()

    redirect_url = 'staff:vendedor_list' if tipo == 'vendedor' else 'staff:chofer_list'
    return redirect(redirect_url)


@require_POST
@login_required
def eliminar_staff(request, tipo, pk):
    Model = Vendedor if tipo == 'vendedor' else Chofer
    staff = get_object_or_404(Model, pk=pk)
    staff.delete()
    
    redirect_url = 'staff:vendedor_list' if tipo == 'vendedor' else 'staff:chofer_list'
    return redirect(redirect_url)