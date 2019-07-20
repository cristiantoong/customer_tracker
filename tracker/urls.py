from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.home, name='home'),
    path('additem/', views.add_item, name='add_item'),
    path('<int:item_id>/', views.item_detail, name='item_detail'),
    path('<int:item_id>/update/', views.update_item, name='update_item'),

]
