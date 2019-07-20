from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.home, name='home'),
    path('additem/', views.add_item, name='add_item'),

]
