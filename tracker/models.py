from django.db import models
from datetime import datetime


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField()
    date_published = models.DateTimeField(default=datetime.now)
    date_expiry = models.DateTimeField(blank=True, null=True)
    date_tracked = models.DateTimeField(blank=True, null=True)
    is_claimed = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_name
