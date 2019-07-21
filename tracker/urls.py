from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.home, name='home'),
    path('additem/', views.add_item, name='add_item'),
    path('<int:item_id>/', views.item_detail, name='item_detail'),
    path('<int:item_id>/update/', views.update_item, name='update_item'),
    path('<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('import_export/', views.import_export, name='import_export'),
    path('export/xls/', views.export_customer_xls, name='export_customer_xls'),

]
