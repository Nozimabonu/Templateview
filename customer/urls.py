from django.urls import path

from customer.views.auth import login_page, logout_page, register_page
# from customer.views.customers import customers, add_customer, delete_customer, edit_customer, export_data
from customer.views.customers import CustomersListView, CustomersAddListView, CustomerDeleteView, CustomerUpdateView, export_data

urlpatterns = [
    path('customer-list/', CustomersListView.as_view(), name='customers'),
    path('add-customer/', CustomersAddListView.as_view(), name='add_customer'),
    path('customer/<int:pk>/delete', CustomerDeleteView.as_view(), name='delete'),
    path('customer/<int:pk>/update', CustomerUpdateView.as_view(), name='edit'),
    # Authentication path
    path('login-page/', login_page, name='login'),
    path('logout-page/', logout_page, name='logout'),
    path('register-page/', register_page, name='register'),
    path('export-data/', export_data, name='export_data')
]
