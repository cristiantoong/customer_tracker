from django.forms import ModelForm, DateTimeInput
from .models import Customer


class DateTimeInput(DateTimeInput):
    input_type = 'date'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        # fields = ['customer_name', 'address', 'product', 'price',
        #           'date_published', 'date_expiry', 'date_tracked', 'is_claimed']
        fields = '__all__'
        widgets = {
            'date_published': DateTimeInput(attrs={'type': 'date'}),
            'date_expiry': DateTimeInput(attrs={'type': 'date'}),
            'date_tracked': DateTimeInput(attrs={'type': 'date'}),
        }
