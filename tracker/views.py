from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import CustomerForm
from django.contrib import messages


@login_required
def home(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'tracker/home.html', context)


@login_required
def add_item(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added Customer Successfully')
            return redirect('tracker:add_item')
    else:
        form = CustomerForm()

    context = {'form': form}
    return render(request, 'tracker/add_item.html', context)


def item_detail(request, item_id):
    item = get_object_or_404(Customer, pk=item_id)
    context = {'item': item}
    return render(request, 'tracker/item_detail.html', context)


def update_item(request, item_id):
    customer = get_object_or_404(Customer, pk=item_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item Updated')
            return redirect('tracker:home')
    else:
        form = CustomerForm(instance=customer)
    context = {
        'form': form,
        'customer': customer,
    }
    return render(request, 'tracker/item_update.html', context)
