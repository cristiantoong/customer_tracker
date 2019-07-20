from django.contrib import admin
from django.urls import path, include
from . import views


app_name ='customer_tracker'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    # path('', views.home, name='home'),
    # path('', views.home, name='home'),
    path('', include('accounts.urls')),
    path('tracker/', include('tracker.urls')),
]
