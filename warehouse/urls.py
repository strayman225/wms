# urls.py
from django.conf import settings
from django.views.static import serve
from django.urls import include, path, re_path
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [

    path('main/', index, name='index_html'),
    path('', auth_views.LoginView.as_view(template_name='warehouse/login.html'), name='login'),
    path('products/', product_list, name='product_list'),
    path('warehouses/', warehouse_list, name='warehouse_list'),
    path('warehouses/<int:warehouse_id>/', stock_list, name='stock_list'),
    path('incoming/', incoming, name='incoming_html'),
    path('outgoing/', outgoing, name='outgoing_html'),
    path('search/', BootstrapFilterView , name='Search_html'),
    path('list/', record_list , name='list_html'),
    path('summary/', summary_list, name='summary_html'),
    path('itemhistory/<str:pk>', single_record_list, name='single_list'),
    path('logout/', logout_view, name='logout'),
    
      
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    