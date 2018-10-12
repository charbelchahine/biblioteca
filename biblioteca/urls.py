from django.urls import path
from . import views
from django.conf.urls import handler403
from django.views.generic import RedirectView
from . import ___django_rest_api_vtk_log___

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_request, name='login'),
    path('logout', views.end_session, name='logout'),
    path('admin', views.admin_landing, name='admin_landing'),
    path('admin/register', views.register_user, name='admin_register'),
    path('admin/users', views.get_users, name='admin_user_list'),
    path('admin/items', views.get_items, name='admin_view_items'),
    path('admin/add_item/<slug:item_type>', views.add_item, name='admin_add_item'),
    path('admin/delete_item', views.item_delete, name='admin_delete_items'),
    path('admin/edit_item/<slug:item_type>/<int:item_id>', views.edit_item, name='admin_edit_item'),
    path('landing', views.client_landing, name='client_area'),
    path('api/slack/vtk', ___django_rest_api_vtk_log___.vtk_logger, name='vtkapi')
]

handler403='biblioteca.views.permission_denied'