# views.py

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import *
from .forms import *
from django.core.paginator import Paginator





def product_list(request):
    products = Product.objects.all()
    return render(request, 'warehouse/product_list.html', {'products': products})

def warehouse_list(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'warehouse/warehouse_list.html', {'warehouses': warehouses})

def stock_list(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    stocks = Items.objects.filter(warehouse=warehouse)
    return render(request, 'warehouse/stock_list.html', {'warehouse': warehouse, 'stocks': stocks})


def incoming(request):
    form = IncomingForm()
    if request.method == "POST":
        form = IncomingForm(request.POST)
        if form.is_valid():
            form.save()
            records = Transaction.objects.values('item__stockname','item__critical','item__id').annotate(
                total_stock=Sum('qtyIN')-Sum('qtyout'),
                difference =F('item__critical')-F('total_stock')
                ).order_by('-difference')
            return render(request, 'warehouse/summary.html', {'records': records})

    context = {'form':form}
    return render(request,'warehouse/incoming.html',context)

def outgoing(request):
    form = OutgoingForm()
    if request.method == "POST":
        form = OutgoingForm(request.POST)
        if form.is_valid():
            form.save()
            records = Transaction.objects.values('item__stockname','item__critical','item__id').annotate(
                total_stock=Sum('qtyIN')-Sum('qtyout'),
                difference =F('item__critical')-F('total_stock')
                ).order_by('-difference')
            return render(request, 'warehouse/summary.html', {'records': records})
    context = {'form':form}
    return render(request,'warehouse/issuance.html',context)


def BootstrapFilterView(request):
    title_contains = request.GET.get('title_contains')

    print(title_contains)
    return render(request, "warehouse/search.html", {})


def record_list(request):
    records = Transaction.objects.all()
    total_delivered = sum(record.qtyIN for record in records)
    total_issued = sum(record.qtyout for record in records)
    total_stock = sum(record.qtyIN for record in records) - sum(record.qtyout for record in records)
    return render(request, 'warehouse/list.html', {'records': records, 'total_delivered': total_delivered,'total_issued': total_issued,'total_stock': total_stock})

from django.db.models import Sum,F

def summary_list(request):
    records = Transaction.objects.values('item__stockname','item__critical','item__id').annotate(
        total_stock=Sum('qtyIN')-Sum('qtyout'),
        difference =F('item__critical')-F('total_stock')
        ).order_by('-difference')

    return render(request, 'warehouse/summary.html', {'records': records})


def index(request):
    return render(request, 'warehouse/index.html')

from django.urls import reverse
from django.views import View


class YourFilteredView(View):
    def get(self, request):
        # Retrieve query parameters from the request
        category = request.GET.get('item')       

        # Filter queryset based on query parameters
        queryset = Transaction.objects.filter(item=category)

        return render(request, 'warehouse/list_single.html', {'records': queryset})


def single_record_list(request, pk):
    item = Items.objects.get(id=pk)

    records = Transaction.objects.filter(item=item).order_by('-transdate')
    
    p = Paginator(Transaction.objects.filter(item=item).order_by('-transdate'),10)
    page = request.GET.get('page')
    lists = p.get_page(page)


    firstrec = records.first 

    total_delivered = sum(record.qtyIN for record in records)
    total_issued = sum(record.qtyout for record in records)
    total_stock = sum(record.qtyIN for record in records) - sum(record.qtyout for record in records)
    return render(request, 'warehouse/list_single.html', {'records': records, 'total_delivered': total_delivered,'total_issued': total_issued,'total_stock': total_stock,'firstrec': firstrec,'lists':lists}) 
