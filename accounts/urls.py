from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

app_name = 'accounts'

urlpatterns = [
    path('', user_views.home_view, name='home_view'),
    path('login/', user_views.signin, name='signin'),
    path('logout/', user_views.logout_view, name='logout'),
    path('register/', user_views.register, name='register'),

]
