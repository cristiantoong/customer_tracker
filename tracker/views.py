from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import CustomerForm
from django.contrib import messages
import xlwt


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


@login_required
def item_detail(request, item_id):
    item = get_object_or_404(Customer, pk=item_id)
    context = {'item': item}
    return render(request, 'tracker/item_detail.html', context)


@login_required
def update_item(request, item_id):
    customer = get_object_or_404(Customer, pk=item_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item Successfully Updated')
            return redirect('tracker:home')
    else:
        form = CustomerForm(instance=customer)
    context = {
        'form': form,
        'customer': customer,
    }
    return render(request, 'tracker/item_update.html', context)


@login_required
def delete_item(request, item_id):
    customer = get_object_or_404(Customer, pk=item_id)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Item Successfully Deleted')
        return redirect('tracker:home')
    context = {
        'customer': customer
    }
    return render(request, 'tracker/item_delete.html', context)


def export_customer_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=".xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Customer')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Customer', 'Address', 'Product', 'Price']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Customer.objects.all().values_list('customer_name', 'address',
                                              'product', 'price')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def import_export(request):
    return render(request, 'tracker/import_export.html')
