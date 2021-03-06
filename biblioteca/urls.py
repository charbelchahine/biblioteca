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
    path('admin/loan_history', views.get_loan_history, name='admin_loan_history'),
    path('client', views.client_landing, name='client_landing'),
    path('client/items', views.get_items, name='client_view_items'),
    path('client/add_to_cart', views.add_to_cart, name='client_add_to_cart'),
    path('client/remove_from_cart', views.delete_from_cart, name='client_remove_from_cart'),
    path('client/cart', views.view_cart, name='client_view_cart'),
    path('client/checkout', views.checkout, name='client_checkout'),
    path('client/return_item', views.return_loan, name='client_return_item'),
    path('client/view_loans', views.get_loans, name='client_view_loans'),
    path('api/slack/vtk', ___django_rest_api_vtk_log___.vtk_logger, name='vtkapi')
]

handler403='biblioteca.views.permission_denied'