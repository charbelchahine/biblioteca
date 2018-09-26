from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_request, name='login'),
    path('logout', views.end_session, name='logout'),
    path('admin_landing', views.admin_landing, name='admin'),
    # path('client', views.client_landing, name='client area')
]