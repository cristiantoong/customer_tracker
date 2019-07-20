from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Customer

@login_required
def home(request):
    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request, 'tracker/home.html', context)


@login_required
def add_item(request):

    # context = {'form':form}
    return render(request, 'tracker/add_item.html', {})
