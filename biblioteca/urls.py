from django.urls import path
from . import views
from django.conf.urls import handler403

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_request, name='login'),
    path('logout', views.end_session, name='logout'),
    path('admin', views.admin_landing, name='admin_landing'),
    path('admin/register', views.register_user, name='admin_register'),
    path('admin/users', views.get_users, name='admin_user_list'),
    path('landing', views.client_landing, name='client_area'),
]

handler403='biblioteca.views.permission_denied'