# urls.py

from django.urls import path
from .views import *
urlpatterns = [

    path('', index, name='index_html'),
    path('products/', product_list, name='product_list'),
    path('warehouses/', warehouse_list, name='warehouse_list'),
    path('warehouses/<int:warehouse_id>/', stock_list, name='stock_list'),
    path('incoming/', incoming, name='incoming_html'),
    path('outgoing/', outgoing, name='outgoing_html'),
    path('search/', BootstrapFilterView , name='Search_html'),
    path('list/', record_list , name='list_html'),
    path('summary/', summary_list, name='summary_html'),
    path('itemhistory/<str:pk>', single_record_list, name='single_list'),
]
